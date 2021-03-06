#!/bin/bash

# Only run on the production app
if [ "$ENVIRONMENT" != "production" ];then exit 0; fi

# Install the latest psql client
dbclient-fetcher psql

export SRC_DB_URL=$DATABASE_URL
export DEST_DB_URL=$METABASE_DB_URL

# mb_structure
psql $SRC_DB_URL -c "DROP TABLE IF EXISTS mb_structure"
psql $SRC_DB_URL -c "
CREATE TABLE mb_structure AS
SELECT *
   FROM structures_structure"
psql $SRC_DB_URL -c "ALTER TABLE mb_structure ADD PRIMARY KEY (id)"

pg_dump $DATABASE_URL -O -t mb_structure -c | psql $DEST_DB_URL


# mb_all_service
psql $SRC_DB_URL -c "DROP TABLE IF EXISTS mb_all_service CASCADE"
psql $SRC_DB_URL -c "
CREATE TABLE mb_all_service AS
 SELECT services_service.id,
    services_service.name,
    services_service.short_desc,
    services_service.full_desc,
    services_service.is_cumulative,
    services_service.has_fee,
    services_service.fee_details,
    services_service.beneficiaries_access_modes_other,
    services_service.coach_orientation_modes_other,
    services_service.forms,
    services_service.remote_url,
    services_service.address1,
    services_service.address2,
    services_service.postal_code,
    services_service.city_code,
    services_service.city,
    services_service.recurrence,
    services_service.suspension_date,
    services_service.creation_date,
    services_service.modification_date,
    services_service.creator_id,
    services_service.last_editor_id,
    services_service.structure_id,
    services_service.slug,
    services_service.online_form,
    -- TODO: deprecated
    (select services_service.status!='PUBLISHED') AS is_draft,
    (select services_service.status='SUGGESTION') AS is_suggestion,
    --
    services_service.status,
    services_service.publication_date,
    services_service.diffusion_zone_details,
    services_service.diffusion_zone_type,
    services_service.qpv_or_zrr,
    services_service.is_model,
    services_service.model_id,
    ( SELECT st_y((services_service.geom)::geometry) AS st_y) AS latitude,
    ( SELECT st_x((services_service.geom)::geometry) AS st_x) AS longitude,
    services_service.last_draft_notification_date,
    services_service.filling_duration,
    services_service.is_contact_info_public,
    (select services_service.contact_name != '') AS has_contact_name,
    (select services_service.contact_phone != '') AS has_contact_phone,
    (select services_service.contact_email != '') AS has_contact_email
   FROM services_service"
psql $SRC_DB_URL -c "ALTER TABLE mb_all_service ADD PRIMARY KEY (id)"



# mb_model. Les mod??les sont des services, mais les self joins sont mal g??r??s sur metabase???
# => on s??pare les deux
psql $SRC_DB_URL -c "DROP VIEW IF EXISTS mb_service"
psql $SRC_DB_URL -c "
CREATE VIEW mb_service AS
 SELECT *
   FROM mb_all_service where is_model is false"

psql $SRC_DB_URL -c "DROP VIEW IF EXISTS mb_model"
psql $SRC_DB_URL -c "
CREATE VIEW mb_model AS
 SELECT *
   FROM mb_all_service where is_model is true"

pg_dump $DATABASE_URL -O -t mb_all_service -t mb_model -t mb_service -c | psql $DEST_DB_URL

# mb_service_suggestion
psql $SRC_DB_URL -c "DROP TABLE IF EXISTS mb_service_suggestion"
psql $SRC_DB_URL -c "
CREATE TABLE mb_service_suggestion AS
 SELECT service_suggestions_servicesuggestion.id,
    service_suggestions_servicesuggestion.siret,
    service_suggestions_servicesuggestion.name,
    service_suggestions_servicesuggestion.creation_date,
    service_suggestions_servicesuggestion.creator_id
   FROM service_suggestions_servicesuggestion"
psql $SRC_DB_URL -c "ALTER TABLE mb_service_suggestion ADD PRIMARY KEY (id)"

pg_dump $DATABASE_URL -O -t mb_service_suggestion -c | psql $DEST_DB_URL


# mb_user
psql $SRC_DB_URL -c "DROP TABLE IF EXISTS mb_user"
psql $SRC_DB_URL -c "
CREATE TABLE mb_user AS
 SELECT users_user.id,
    users_user.is_valid,
    users_user.is_staff,
    users_user.is_bizdev,
    users_user.last_login,
    users_user.date_joined,
    users_user.newsletter
   FROM users_user
  WHERE (users_user.is_active IS TRUE)"
psql $SRC_DB_URL -c "ALTER TABLE mb_user ADD PRIMARY KEY (id)"

pg_dump $DATABASE_URL -O -t mb_user -c | psql $DEST_DB_URL

pg_dump $DATABASE_URL -O -t services_accesscondition -t services_beneficiaryaccessmode -t services_coachorientationmode -t services_concernedpublic -t services_credential -t services_locationkind -t services_requirement -t services_service_access_conditions -t services_service_beneficiaries_access_modes -t services_service_categories -t services_service_coach_orientation_modes -t services_service_concerned_public -t services_service_credentials -t services_service_kinds -t services_service_location_kinds -t services_service_requirements -t services_service_subcategories -t services_servicecategory -t services_servicekind -t services_servicemodificationhistoryitem -t services_servicesubcategory -t structures_structuremember -t structures_structureputativemember -t structures_structuresource -t structures_structuretypology -t stats_deploymentstate -c | psql $DEST_DB_URL
