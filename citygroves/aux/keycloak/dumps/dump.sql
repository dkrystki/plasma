--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: admin_event_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.admin_event_entity (
    id character varying(36) NOT NULL,
    admin_event_time bigint,
    realm_id character varying(255),
    operation_type character varying(255),
    auth_realm_id character varying(255),
    auth_client_id character varying(255),
    auth_user_id character varying(255),
    ip_address character varying(255),
    resource_path character varying(2550),
    representation text,
    error character varying(255),
    resource_type character varying(64)
);


ALTER TABLE public.admin_event_entity OWNER TO keycloak;

--
-- Name: associated_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.associated_policy (
    policy_id character varying(36) NOT NULL,
    associated_policy_id character varying(36) NOT NULL
);


ALTER TABLE public.associated_policy OWNER TO keycloak;

--
-- Name: authentication_execution; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authentication_execution (
    id character varying(36) NOT NULL,
    alias character varying(255),
    authenticator character varying(36),
    realm_id character varying(36),
    flow_id character varying(36),
    requirement integer,
    priority integer,
    authenticator_flow boolean DEFAULT false NOT NULL,
    auth_flow_id character varying(36),
    auth_config character varying(36)
);


ALTER TABLE public.authentication_execution OWNER TO keycloak;

--
-- Name: authentication_flow; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authentication_flow (
    id character varying(36) NOT NULL,
    alias character varying(255),
    description character varying(255),
    realm_id character varying(36),
    provider_id character varying(36) DEFAULT 'basic-flow'::character varying NOT NULL,
    top_level boolean DEFAULT false NOT NULL,
    built_in boolean DEFAULT false NOT NULL
);


ALTER TABLE public.authentication_flow OWNER TO keycloak;

--
-- Name: authenticator_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authenticator_config (
    id character varying(36) NOT NULL,
    alias character varying(255),
    realm_id character varying(36)
);


ALTER TABLE public.authenticator_config OWNER TO keycloak;

--
-- Name: authenticator_config_entry; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.authenticator_config_entry (
    authenticator_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.authenticator_config_entry OWNER TO keycloak;

--
-- Name: broker_link; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.broker_link (
    identity_provider character varying(255) NOT NULL,
    storage_provider_id character varying(255),
    realm_id character varying(36) NOT NULL,
    broker_user_id character varying(255),
    broker_username character varying(255),
    token text,
    user_id character varying(255) NOT NULL
);


ALTER TABLE public.broker_link OWNER TO keycloak;

--
-- Name: client; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client (
    id character varying(36) NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    full_scope_allowed boolean DEFAULT false NOT NULL,
    client_id character varying(255),
    not_before integer,
    public_client boolean DEFAULT false NOT NULL,
    secret character varying(255),
    base_url character varying(255),
    bearer_only boolean DEFAULT false NOT NULL,
    management_url character varying(255),
    surrogate_auth_required boolean DEFAULT false NOT NULL,
    realm_id character varying(36),
    protocol character varying(255),
    node_rereg_timeout integer DEFAULT 0,
    frontchannel_logout boolean DEFAULT false NOT NULL,
    consent_required boolean DEFAULT false NOT NULL,
    name character varying(255),
    service_accounts_enabled boolean DEFAULT false NOT NULL,
    client_authenticator_type character varying(255),
    root_url character varying(255),
    description character varying(255),
    registration_token character varying(255),
    standard_flow_enabled boolean DEFAULT true NOT NULL,
    implicit_flow_enabled boolean DEFAULT false NOT NULL,
    direct_access_grants_enabled boolean DEFAULT false NOT NULL,
    always_display_in_console boolean DEFAULT false NOT NULL
);


ALTER TABLE public.client OWNER TO keycloak;

--
-- Name: client_attributes; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_attributes (
    client_id character varying(36) NOT NULL,
    value character varying(4000),
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_attributes OWNER TO keycloak;

--
-- Name: client_auth_flow_bindings; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_auth_flow_bindings (
    client_id character varying(36) NOT NULL,
    flow_id character varying(36),
    binding_name character varying(255) NOT NULL
);


ALTER TABLE public.client_auth_flow_bindings OWNER TO keycloak;

--
-- Name: client_default_roles; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_default_roles (
    client_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.client_default_roles OWNER TO keycloak;

--
-- Name: client_initial_access; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_initial_access (
    id character varying(36) NOT NULL,
    realm_id character varying(36) NOT NULL,
    "timestamp" integer,
    expiration integer,
    count integer,
    remaining_count integer
);


ALTER TABLE public.client_initial_access OWNER TO keycloak;

--
-- Name: client_node_registrations; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_node_registrations (
    client_id character varying(36) NOT NULL,
    value integer,
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_node_registrations OWNER TO keycloak;

--
-- Name: client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope (
    id character varying(36) NOT NULL,
    name character varying(255),
    realm_id character varying(36),
    description character varying(255),
    protocol character varying(255)
);


ALTER TABLE public.client_scope OWNER TO keycloak;

--
-- Name: client_scope_attributes; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_attributes (
    scope_id character varying(36) NOT NULL,
    value character varying(2048),
    name character varying(255) NOT NULL
);


ALTER TABLE public.client_scope_attributes OWNER TO keycloak;

--
-- Name: client_scope_client; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_client (
    client_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL,
    default_scope boolean DEFAULT false NOT NULL
);


ALTER TABLE public.client_scope_client OWNER TO keycloak;

--
-- Name: client_scope_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_scope_role_mapping (
    scope_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.client_scope_role_mapping OWNER TO keycloak;

--
-- Name: client_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session (
    id character varying(36) NOT NULL,
    client_id character varying(36),
    redirect_uri character varying(255),
    state character varying(255),
    "timestamp" integer,
    session_id character varying(36),
    auth_method character varying(255),
    realm_id character varying(255),
    auth_user_id character varying(36),
    current_action character varying(36)
);


ALTER TABLE public.client_session OWNER TO keycloak;

--
-- Name: client_session_auth_status; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_auth_status (
    authenticator character varying(36) NOT NULL,
    status integer,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_auth_status OWNER TO keycloak;

--
-- Name: client_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_note (
    name character varying(255) NOT NULL,
    value character varying(255),
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_note OWNER TO keycloak;

--
-- Name: client_session_prot_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_prot_mapper (
    protocol_mapper_id character varying(36) NOT NULL,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_prot_mapper OWNER TO keycloak;

--
-- Name: client_session_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_session_role (
    role_id character varying(255) NOT NULL,
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_session_role OWNER TO keycloak;

--
-- Name: client_user_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.client_user_session_note (
    name character varying(255) NOT NULL,
    value character varying(2048),
    client_session character varying(36) NOT NULL
);


ALTER TABLE public.client_user_session_note OWNER TO keycloak;

--
-- Name: component; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.component (
    id character varying(36) NOT NULL,
    name character varying(255),
    parent_id character varying(36),
    provider_id character varying(36),
    provider_type character varying(255),
    realm_id character varying(36),
    sub_type character varying(255)
);


ALTER TABLE public.component OWNER TO keycloak;

--
-- Name: component_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.component_config (
    id character varying(36) NOT NULL,
    component_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(4000)
);


ALTER TABLE public.component_config OWNER TO keycloak;

--
-- Name: composite_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.composite_role (
    composite character varying(36) NOT NULL,
    child_role character varying(36) NOT NULL
);


ALTER TABLE public.composite_role OWNER TO keycloak;

--
-- Name: credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.credential (
    id character varying(36) NOT NULL,
    salt bytea,
    type character varying(255),
    user_id character varying(36),
    created_date bigint,
    user_label character varying(255),
    secret_data text,
    credential_data text,
    priority integer
);


ALTER TABLE public.credential OWNER TO keycloak;

--
-- Name: databasechangelog; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


ALTER TABLE public.databasechangelog OWNER TO keycloak;

--
-- Name: databasechangeloglock; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


ALTER TABLE public.databasechangeloglock OWNER TO keycloak;

--
-- Name: default_client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.default_client_scope (
    realm_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL,
    default_scope boolean DEFAULT false NOT NULL
);


ALTER TABLE public.default_client_scope OWNER TO keycloak;

--
-- Name: event_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.event_entity (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    details_json character varying(2550),
    error character varying(255),
    ip_address character varying(255),
    realm_id character varying(255),
    session_id character varying(255),
    event_time bigint,
    type character varying(255),
    user_id character varying(255)
);


ALTER TABLE public.event_entity OWNER TO keycloak;

--
-- Name: fed_user_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_attribute (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    value character varying(2024)
);


ALTER TABLE public.fed_user_attribute OWNER TO keycloak;

--
-- Name: fed_user_consent; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_consent (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    created_date bigint,
    last_updated_date bigint,
    client_storage_provider character varying(36),
    external_client_id character varying(255)
);


ALTER TABLE public.fed_user_consent OWNER TO keycloak;

--
-- Name: fed_user_consent_cl_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_consent_cl_scope (
    user_consent_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.fed_user_consent_cl_scope OWNER TO keycloak;

--
-- Name: fed_user_credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_credential (
    id character varying(36) NOT NULL,
    salt bytea,
    type character varying(255),
    created_date bigint,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36),
    user_label character varying(255),
    secret_data text,
    credential_data text,
    priority integer
);


ALTER TABLE public.fed_user_credential OWNER TO keycloak;

--
-- Name: fed_user_group_membership; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_group_membership (
    group_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_group_membership OWNER TO keycloak;

--
-- Name: fed_user_required_action; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_required_action (
    required_action character varying(255) DEFAULT ' '::character varying NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_required_action OWNER TO keycloak;

--
-- Name: fed_user_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.fed_user_role_mapping (
    role_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    storage_provider_id character varying(36)
);


ALTER TABLE public.fed_user_role_mapping OWNER TO keycloak;

--
-- Name: federated_identity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.federated_identity (
    identity_provider character varying(255) NOT NULL,
    realm_id character varying(36),
    federated_user_id character varying(255),
    federated_username character varying(255),
    token text,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.federated_identity OWNER TO keycloak;

--
-- Name: federated_user; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.federated_user (
    id character varying(255) NOT NULL,
    storage_provider_id character varying(255),
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.federated_user OWNER TO keycloak;

--
-- Name: group_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.group_attribute (
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255),
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.group_attribute OWNER TO keycloak;

--
-- Name: group_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.group_role_mapping (
    role_id character varying(36) NOT NULL,
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.group_role_mapping OWNER TO keycloak;

--
-- Name: identity_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider (
    internal_id character varying(36) NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    provider_alias character varying(255),
    provider_id character varying(255),
    store_token boolean DEFAULT false NOT NULL,
    authenticate_by_default boolean DEFAULT false NOT NULL,
    realm_id character varying(36),
    add_token_role boolean DEFAULT true NOT NULL,
    trust_email boolean DEFAULT false NOT NULL,
    first_broker_login_flow_id character varying(36),
    post_broker_login_flow_id character varying(36),
    provider_display_name character varying(255),
    link_only boolean DEFAULT false NOT NULL
);


ALTER TABLE public.identity_provider OWNER TO keycloak;

--
-- Name: identity_provider_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider_config (
    identity_provider_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.identity_provider_config OWNER TO keycloak;

--
-- Name: identity_provider_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.identity_provider_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    idp_alias character varying(255) NOT NULL,
    idp_mapper_name character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.identity_provider_mapper OWNER TO keycloak;

--
-- Name: idp_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.idp_mapper_config (
    idp_mapper_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.idp_mapper_config OWNER TO keycloak;

--
-- Name: keycloak_group; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.keycloak_group (
    id character varying(36) NOT NULL,
    name character varying(255),
    parent_group character varying(36),
    realm_id character varying(36)
);


ALTER TABLE public.keycloak_group OWNER TO keycloak;

--
-- Name: keycloak_role; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.keycloak_role (
    id character varying(36) NOT NULL,
    client_realm_constraint character varying(255),
    client_role boolean DEFAULT false NOT NULL,
    description character varying(255),
    name character varying(255),
    realm_id character varying(255),
    client character varying(36),
    realm character varying(36)
);


ALTER TABLE public.keycloak_role OWNER TO keycloak;

--
-- Name: migration_model; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.migration_model (
    id character varying(36) NOT NULL,
    version character varying(36),
    update_time bigint DEFAULT 0 NOT NULL
);


ALTER TABLE public.migration_model OWNER TO keycloak;

--
-- Name: offline_client_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.offline_client_session (
    user_session_id character varying(36) NOT NULL,
    client_id character varying(255) NOT NULL,
    offline_flag character varying(4) NOT NULL,
    "timestamp" integer,
    data text,
    client_storage_provider character varying(36) DEFAULT 'local'::character varying NOT NULL,
    external_client_id character varying(255) DEFAULT 'local'::character varying NOT NULL
);


ALTER TABLE public.offline_client_session OWNER TO keycloak;

--
-- Name: offline_user_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.offline_user_session (
    user_session_id character varying(36) NOT NULL,
    user_id character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL,
    created_on integer NOT NULL,
    offline_flag character varying(4) NOT NULL,
    data text,
    last_session_refresh integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.offline_user_session OWNER TO keycloak;

--
-- Name: policy_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.policy_config (
    policy_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value text
);


ALTER TABLE public.policy_config OWNER TO keycloak;

--
-- Name: protocol_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.protocol_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    protocol character varying(255) NOT NULL,
    protocol_mapper_name character varying(255) NOT NULL,
    client_id character varying(36),
    client_scope_id character varying(36)
);


ALTER TABLE public.protocol_mapper OWNER TO keycloak;

--
-- Name: protocol_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.protocol_mapper_config (
    protocol_mapper_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.protocol_mapper_config OWNER TO keycloak;

--
-- Name: realm; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm (
    id character varying(36) NOT NULL,
    access_code_lifespan integer,
    user_action_lifespan integer,
    access_token_lifespan integer,
    account_theme character varying(255),
    admin_theme character varying(255),
    email_theme character varying(255),
    enabled boolean DEFAULT false NOT NULL,
    events_enabled boolean DEFAULT false NOT NULL,
    events_expiration bigint,
    login_theme character varying(255),
    name character varying(255),
    not_before integer,
    password_policy character varying(2550),
    registration_allowed boolean DEFAULT false NOT NULL,
    remember_me boolean DEFAULT false NOT NULL,
    reset_password_allowed boolean DEFAULT false NOT NULL,
    social boolean DEFAULT false NOT NULL,
    ssl_required character varying(255),
    sso_idle_timeout integer,
    sso_max_lifespan integer,
    update_profile_on_soc_login boolean DEFAULT false NOT NULL,
    verify_email boolean DEFAULT false NOT NULL,
    master_admin_client character varying(36),
    login_lifespan integer,
    internationalization_enabled boolean DEFAULT false NOT NULL,
    default_locale character varying(255),
    reg_email_as_username boolean DEFAULT false NOT NULL,
    admin_events_enabled boolean DEFAULT false NOT NULL,
    admin_events_details_enabled boolean DEFAULT false NOT NULL,
    edit_username_allowed boolean DEFAULT false NOT NULL,
    otp_policy_counter integer DEFAULT 0,
    otp_policy_window integer DEFAULT 1,
    otp_policy_period integer DEFAULT 30,
    otp_policy_digits integer DEFAULT 6,
    otp_policy_alg character varying(36) DEFAULT 'HmacSHA1'::character varying,
    otp_policy_type character varying(36) DEFAULT 'totp'::character varying,
    browser_flow character varying(36),
    registration_flow character varying(36),
    direct_grant_flow character varying(36),
    reset_credentials_flow character varying(36),
    client_auth_flow character varying(36),
    offline_session_idle_timeout integer DEFAULT 0,
    revoke_refresh_token boolean DEFAULT false NOT NULL,
    access_token_life_implicit integer DEFAULT 0,
    login_with_email_allowed boolean DEFAULT true NOT NULL,
    duplicate_emails_allowed boolean DEFAULT false NOT NULL,
    docker_auth_flow character varying(36),
    refresh_token_max_reuse integer DEFAULT 0,
    allow_user_managed_access boolean DEFAULT false NOT NULL,
    sso_max_lifespan_remember_me integer DEFAULT 0 NOT NULL,
    sso_idle_timeout_remember_me integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.realm OWNER TO keycloak;

--
-- Name: realm_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_attribute (
    name character varying(255) NOT NULL,
    value character varying(255),
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_attribute OWNER TO keycloak;

--
-- Name: realm_default_groups; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_default_groups (
    realm_id character varying(36) NOT NULL,
    group_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_default_groups OWNER TO keycloak;

--
-- Name: realm_default_roles; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_default_roles (
    realm_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_default_roles OWNER TO keycloak;

--
-- Name: realm_enabled_event_types; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_enabled_event_types (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_enabled_event_types OWNER TO keycloak;

--
-- Name: realm_events_listeners; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_events_listeners (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_events_listeners OWNER TO keycloak;

--
-- Name: realm_required_credential; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_required_credential (
    type character varying(255) NOT NULL,
    form_label character varying(255),
    input boolean DEFAULT false NOT NULL,
    secret boolean DEFAULT false NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.realm_required_credential OWNER TO keycloak;

--
-- Name: realm_smtp_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_smtp_config (
    realm_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.realm_smtp_config OWNER TO keycloak;

--
-- Name: realm_supported_locales; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.realm_supported_locales (
    realm_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.realm_supported_locales OWNER TO keycloak;

--
-- Name: redirect_uris; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.redirect_uris (
    client_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.redirect_uris OWNER TO keycloak;

--
-- Name: required_action_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.required_action_config (
    required_action_id character varying(36) NOT NULL,
    value text,
    name character varying(255) NOT NULL
);


ALTER TABLE public.required_action_config OWNER TO keycloak;

--
-- Name: required_action_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.required_action_provider (
    id character varying(36) NOT NULL,
    alias character varying(255),
    name character varying(255),
    realm_id character varying(36),
    enabled boolean DEFAULT false NOT NULL,
    default_action boolean DEFAULT false NOT NULL,
    provider_id character varying(255),
    priority integer
);


ALTER TABLE public.required_action_provider OWNER TO keycloak;

--
-- Name: resource_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_attribute (
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255),
    resource_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_attribute OWNER TO keycloak;

--
-- Name: resource_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_policy (
    resource_id character varying(36) NOT NULL,
    policy_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_policy OWNER TO keycloak;

--
-- Name: resource_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_scope (
    resource_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.resource_scope OWNER TO keycloak;

--
-- Name: resource_server; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server (
    id character varying(36) NOT NULL,
    allow_rs_remote_mgmt boolean DEFAULT false NOT NULL,
    policy_enforce_mode character varying(15) NOT NULL,
    decision_strategy smallint DEFAULT 1 NOT NULL
);


ALTER TABLE public.resource_server OWNER TO keycloak;

--
-- Name: resource_server_perm_ticket; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_perm_ticket (
    id character varying(36) NOT NULL,
    owner character varying(255) NOT NULL,
    requester character varying(255) NOT NULL,
    created_timestamp bigint NOT NULL,
    granted_timestamp bigint,
    resource_id character varying(36) NOT NULL,
    scope_id character varying(36),
    resource_server_id character varying(36) NOT NULL,
    policy_id character varying(36)
);


ALTER TABLE public.resource_server_perm_ticket OWNER TO keycloak;

--
-- Name: resource_server_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_policy (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(255),
    type character varying(255) NOT NULL,
    decision_strategy character varying(20),
    logic character varying(20),
    resource_server_id character varying(36) NOT NULL,
    owner character varying(255)
);


ALTER TABLE public.resource_server_policy OWNER TO keycloak;

--
-- Name: resource_server_resource; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_resource (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(255),
    icon_uri character varying(255),
    owner character varying(255) NOT NULL,
    resource_server_id character varying(36) NOT NULL,
    owner_managed_access boolean DEFAULT false NOT NULL,
    display_name character varying(255)
);


ALTER TABLE public.resource_server_resource OWNER TO keycloak;

--
-- Name: resource_server_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_server_scope (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    icon_uri character varying(255),
    resource_server_id character varying(36) NOT NULL,
    display_name character varying(255)
);


ALTER TABLE public.resource_server_scope OWNER TO keycloak;

--
-- Name: resource_uris; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.resource_uris (
    resource_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.resource_uris OWNER TO keycloak;

--
-- Name: role_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.role_attribute (
    id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(255)
);


ALTER TABLE public.role_attribute OWNER TO keycloak;

--
-- Name: scope_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.scope_mapping (
    client_id character varying(36) NOT NULL,
    role_id character varying(36) NOT NULL
);


ALTER TABLE public.scope_mapping OWNER TO keycloak;

--
-- Name: scope_policy; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.scope_policy (
    scope_id character varying(36) NOT NULL,
    policy_id character varying(36) NOT NULL
);


ALTER TABLE public.scope_policy OWNER TO keycloak;

--
-- Name: user_attribute; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_attribute (
    name character varying(255) NOT NULL,
    value character varying(255),
    user_id character varying(36) NOT NULL,
    id character varying(36) DEFAULT 'sybase-needs-something-here'::character varying NOT NULL
);


ALTER TABLE public.user_attribute OWNER TO keycloak;

--
-- Name: user_consent; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_consent (
    id character varying(36) NOT NULL,
    client_id character varying(255),
    user_id character varying(36) NOT NULL,
    created_date bigint,
    last_updated_date bigint,
    client_storage_provider character varying(36),
    external_client_id character varying(255)
);


ALTER TABLE public.user_consent OWNER TO keycloak;

--
-- Name: user_consent_client_scope; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_consent_client_scope (
    user_consent_id character varying(36) NOT NULL,
    scope_id character varying(36) NOT NULL
);


ALTER TABLE public.user_consent_client_scope OWNER TO keycloak;

--
-- Name: user_entity; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_entity (
    id character varying(36) NOT NULL,
    email character varying(255),
    email_constraint character varying(255),
    email_verified boolean DEFAULT false NOT NULL,
    enabled boolean DEFAULT false NOT NULL,
    federation_link character varying(255),
    first_name character varying(255),
    last_name character varying(255),
    realm_id character varying(255),
    username character varying(255),
    created_timestamp bigint,
    service_account_client_link character varying(255),
    not_before integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.user_entity OWNER TO keycloak;

--
-- Name: user_federation_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_config (
    user_federation_provider_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.user_federation_config OWNER TO keycloak;

--
-- Name: user_federation_mapper; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_mapper (
    id character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    federation_provider_id character varying(36) NOT NULL,
    federation_mapper_type character varying(255) NOT NULL,
    realm_id character varying(36) NOT NULL
);


ALTER TABLE public.user_federation_mapper OWNER TO keycloak;

--
-- Name: user_federation_mapper_config; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_mapper_config (
    user_federation_mapper_id character varying(36) NOT NULL,
    value character varying(255),
    name character varying(255) NOT NULL
);


ALTER TABLE public.user_federation_mapper_config OWNER TO keycloak;

--
-- Name: user_federation_provider; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_federation_provider (
    id character varying(36) NOT NULL,
    changed_sync_period integer,
    display_name character varying(255),
    full_sync_period integer,
    last_sync integer,
    priority integer,
    provider_name character varying(255),
    realm_id character varying(36)
);


ALTER TABLE public.user_federation_provider OWNER TO keycloak;

--
-- Name: user_group_membership; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_group_membership (
    group_id character varying(36) NOT NULL,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.user_group_membership OWNER TO keycloak;

--
-- Name: user_required_action; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_required_action (
    user_id character varying(36) NOT NULL,
    required_action character varying(255) DEFAULT ' '::character varying NOT NULL
);


ALTER TABLE public.user_required_action OWNER TO keycloak;

--
-- Name: user_role_mapping; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_role_mapping (
    role_id character varying(255) NOT NULL,
    user_id character varying(36) NOT NULL
);


ALTER TABLE public.user_role_mapping OWNER TO keycloak;

--
-- Name: user_session; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_session (
    id character varying(36) NOT NULL,
    auth_method character varying(255),
    ip_address character varying(255),
    last_session_refresh integer,
    login_username character varying(255),
    realm_id character varying(255),
    remember_me boolean DEFAULT false NOT NULL,
    started integer,
    user_id character varying(255),
    user_session_state integer,
    broker_session_id character varying(255),
    broker_user_id character varying(255)
);


ALTER TABLE public.user_session OWNER TO keycloak;

--
-- Name: user_session_note; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.user_session_note (
    user_session character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    value character varying(2048)
);


ALTER TABLE public.user_session_note OWNER TO keycloak;

--
-- Name: username_login_failure; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.username_login_failure (
    realm_id character varying(36) NOT NULL,
    username character varying(255) NOT NULL,
    failed_login_not_before integer,
    last_failure bigint,
    last_ip_failure character varying(255),
    num_failures integer
);


ALTER TABLE public.username_login_failure OWNER TO keycloak;

--
-- Name: web_origins; Type: TABLE; Schema: public; Owner: keycloak
--

CREATE TABLE public.web_origins (
    client_id character varying(36) NOT NULL,
    value character varying(255) NOT NULL
);


ALTER TABLE public.web_origins OWNER TO keycloak;

--
-- Data for Name: admin_event_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.admin_event_entity (id, admin_event_time, realm_id, operation_type, auth_realm_id, auth_client_id, auth_user_id, ip_address, resource_path, representation, error, resource_type) FROM stdin;
\.


--
-- Data for Name: associated_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.associated_policy (policy_id, associated_policy_id) FROM stdin;
\.


--
-- Data for Name: authentication_execution; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authentication_execution (id, alias, authenticator, realm_id, flow_id, requirement, priority, authenticator_flow, auth_flow_id, auth_config) FROM stdin;
17955433-e8ad-4570-9c40-0cd4b7ab9b14	\N	auth-cookie	master	79490408-8ca6-4c72-8065-c1f2979a54ac	2	10	f	\N	\N
ddccad84-a28e-493b-a9e9-378f246cad43	\N	auth-spnego	master	79490408-8ca6-4c72-8065-c1f2979a54ac	3	20	f	\N	\N
c774437b-6149-4ce2-9626-cd962a5c0a13	\N	identity-provider-redirector	master	79490408-8ca6-4c72-8065-c1f2979a54ac	2	25	f	\N	\N
5f25e019-893d-469f-9bf2-e1e7d04588aa	\N	\N	master	79490408-8ca6-4c72-8065-c1f2979a54ac	2	30	t	4a14b992-6617-4174-8b52-72e3f8d99578	\N
ebd41530-168c-4632-9635-5c318551a4e5	\N	auth-username-password-form	master	4a14b992-6617-4174-8b52-72e3f8d99578	0	10	f	\N	\N
42377b7e-a737-47ff-9759-d5cda5eaede7	\N	\N	master	4a14b992-6617-4174-8b52-72e3f8d99578	1	20	t	4789e42a-8381-4575-bea7-85e67898d6f5	\N
94da19d0-7d94-4d6f-9ad3-8d173b140f15	\N	conditional-user-configured	master	4789e42a-8381-4575-bea7-85e67898d6f5	0	10	f	\N	\N
54516f06-1fac-47db-80e7-80ef158630b9	\N	auth-otp-form	master	4789e42a-8381-4575-bea7-85e67898d6f5	0	20	f	\N	\N
d6dfe5a5-ea38-43f7-a17f-96358266c0ae	\N	direct-grant-validate-username	master	9884d6b5-d7f9-476b-a97f-52d9fb506768	0	10	f	\N	\N
120ccf69-013f-4e1f-afcc-729652023fed	\N	direct-grant-validate-password	master	9884d6b5-d7f9-476b-a97f-52d9fb506768	0	20	f	\N	\N
b6f4b1c5-bb66-4e8c-ba02-7de24f506055	\N	\N	master	9884d6b5-d7f9-476b-a97f-52d9fb506768	1	30	t	deee9e90-9891-4ebc-b62d-ce0527845943	\N
70e400c8-ec35-4df3-857a-e7f82cb72430	\N	conditional-user-configured	master	deee9e90-9891-4ebc-b62d-ce0527845943	0	10	f	\N	\N
e1021cb4-3241-4c7f-bb81-372750358c09	\N	direct-grant-validate-otp	master	deee9e90-9891-4ebc-b62d-ce0527845943	0	20	f	\N	\N
0987a4ab-08ae-4726-af46-d097d7745c4e	\N	registration-page-form	master	05359703-bbea-467e-a919-d195f5b5175c	0	10	t	4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	\N
6b8c28fd-8104-48a8-a935-0bfe90f16d5b	\N	registration-user-creation	master	4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	0	20	f	\N	\N
64172655-8d89-474d-857e-abf5b9600afa	\N	registration-profile-action	master	4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	0	40	f	\N	\N
718df60f-85b0-4a3a-ad8c-47fa57033c3e	\N	registration-password-action	master	4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	0	50	f	\N	\N
f697a3e0-44ed-4a20-aec4-208335da7700	\N	registration-recaptcha-action	master	4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	3	60	f	\N	\N
6d2bccc4-f23e-43e3-aa29-60683adc6b94	\N	reset-credentials-choose-user	master	9bf06127-8c95-49e4-a39f-659f818cde5d	0	10	f	\N	\N
520b1293-1380-4bd7-be58-089d54cc0cd5	\N	reset-credential-email	master	9bf06127-8c95-49e4-a39f-659f818cde5d	0	20	f	\N	\N
7bb29a13-f2fe-442b-bffb-2cbb22a1ce95	\N	reset-password	master	9bf06127-8c95-49e4-a39f-659f818cde5d	0	30	f	\N	\N
85c78ddf-aba0-4ad4-8469-69edf0d23d64	\N	\N	master	9bf06127-8c95-49e4-a39f-659f818cde5d	1	40	t	8624d73a-6772-4cf6-9889-7d8f63fad1e7	\N
a5189199-78f4-4f51-adc2-29fa9f7279dc	\N	conditional-user-configured	master	8624d73a-6772-4cf6-9889-7d8f63fad1e7	0	10	f	\N	\N
a90ab80a-b6e1-4dc7-88fb-1d3a1abf9053	\N	reset-otp	master	8624d73a-6772-4cf6-9889-7d8f63fad1e7	0	20	f	\N	\N
959bc2ef-ecb0-4392-bebb-10e58dbf9fec	\N	client-secret	master	b693e22c-d3f3-4c25-8740-5e9e2c4e94db	2	10	f	\N	\N
fada299b-c8c0-4e17-af63-9f3cb4cde8d2	\N	client-jwt	master	b693e22c-d3f3-4c25-8740-5e9e2c4e94db	2	20	f	\N	\N
b31c6b74-20b1-42ba-800c-2a94f7bc131e	\N	client-secret-jwt	master	b693e22c-d3f3-4c25-8740-5e9e2c4e94db	2	30	f	\N	\N
d6fd166d-200e-4eb1-9d2a-9d4ca2ff81b5	\N	client-x509	master	b693e22c-d3f3-4c25-8740-5e9e2c4e94db	2	40	f	\N	\N
c65ed378-7529-41bd-adb4-b479bec87c1f	\N	idp-review-profile	master	3dd9bc4d-94ce-49d2-8fcb-3e5c5ccab86e	0	10	f	\N	f39ebfc7-2655-4231-a678-365eb4b8a1a3
6418cfed-6476-415e-b242-386e7e274348	\N	\N	master	3dd9bc4d-94ce-49d2-8fcb-3e5c5ccab86e	0	20	t	54df3865-4131-4917-a01e-cd964677e365	\N
3d98a91c-7a6f-49c6-a344-ebb0aab3c9bc	\N	idp-create-user-if-unique	master	54df3865-4131-4917-a01e-cd964677e365	2	10	f	\N	f25bc570-c320-4f6c-a154-a8b9924a141d
edd72746-1b32-4065-aa29-6dc584075d50	\N	\N	master	54df3865-4131-4917-a01e-cd964677e365	2	20	t	bf46b9fe-8c0c-42ea-9297-f92f377f173c	\N
b0001e20-c09d-4ea8-9cc2-873608027fab	\N	idp-confirm-link	master	bf46b9fe-8c0c-42ea-9297-f92f377f173c	0	10	f	\N	\N
bc07726a-082b-44d4-9af4-3505b6c3997f	\N	\N	master	bf46b9fe-8c0c-42ea-9297-f92f377f173c	0	20	t	bfaef943-6d4e-4c2b-ac9d-6941584d39f2	\N
6457071b-c026-49e3-8b94-21b908449afa	\N	idp-email-verification	master	bfaef943-6d4e-4c2b-ac9d-6941584d39f2	2	10	f	\N	\N
63330d2c-e39a-4ea5-a7ea-a828dba36cc3	\N	\N	master	bfaef943-6d4e-4c2b-ac9d-6941584d39f2	2	20	t	20aafc04-3629-40c3-ba8a-7592db17eede	\N
9a21da4f-fe2e-403f-98bb-176e02449dab	\N	idp-username-password-form	master	20aafc04-3629-40c3-ba8a-7592db17eede	0	10	f	\N	\N
47aa70b9-cc26-4c5d-9a44-e3bf8ef0ac6a	\N	\N	master	20aafc04-3629-40c3-ba8a-7592db17eede	1	20	t	5d306a1b-44c6-4cd3-99db-ab174526f2eb	\N
86051c36-eb7d-49ea-bba4-2a1befb5c020	\N	conditional-user-configured	master	5d306a1b-44c6-4cd3-99db-ab174526f2eb	0	10	f	\N	\N
6f8bf98f-7e3e-4310-83a8-6f0524361b99	\N	auth-otp-form	master	5d306a1b-44c6-4cd3-99db-ab174526f2eb	0	20	f	\N	\N
b5815f8e-3123-4764-8a34-f4ded7c7cc2b	\N	http-basic-authenticator	master	46a57c26-2bb8-4106-adbd-92ded879ff2e	0	10	f	\N	\N
7f075bf1-042a-4adf-84e9-0aa645022588	\N	docker-http-basic-authenticator	master	4f72d4dd-d825-40a7-91b3-d94247b32937	0	10	f	\N	\N
7400d2b7-9603-4988-810b-ba8152ac5b2b	\N	no-cookie-redirect	master	8e4c4f11-f5bf-412e-8168-68ecf1c73016	0	10	f	\N	\N
2cba3505-9256-46bb-ac88-4bcedaf6476f	\N	\N	master	8e4c4f11-f5bf-412e-8168-68ecf1c73016	0	20	t	45f0509e-8811-43ee-8c05-adfc9586c916	\N
b4d81ae9-d25c-48e4-af62-5e668f627808	\N	basic-auth	master	45f0509e-8811-43ee-8c05-adfc9586c916	0	10	f	\N	\N
aee7dd55-a848-4531-80af-1279a1c9d418	\N	basic-auth-otp	master	45f0509e-8811-43ee-8c05-adfc9586c916	3	20	f	\N	\N
ac5b0ef8-96d9-403a-98ee-543fbce3847a	\N	auth-spnego	master	45f0509e-8811-43ee-8c05-adfc9586c916	3	30	f	\N	\N
4433d675-a48d-44c5-b793-35e64f57c567	\N	auth-cookie	Citygroves	d2818a82-f1db-4276-86fe-246bc5198e12	2	10	f	\N	\N
770be2ab-6c24-4202-9afb-c6d6852aa5fd	\N	auth-spnego	Citygroves	d2818a82-f1db-4276-86fe-246bc5198e12	3	20	f	\N	\N
68b72b4d-594b-4e95-8928-340e24dd6b1a	\N	identity-provider-redirector	Citygroves	d2818a82-f1db-4276-86fe-246bc5198e12	2	25	f	\N	\N
e7e27471-9413-4901-bafd-80554647a283	\N	\N	Citygroves	d2818a82-f1db-4276-86fe-246bc5198e12	2	30	t	8073c234-bfbc-466e-9ab3-84b95fabb6a6	\N
d935be14-b143-419f-9c10-3d78ad6e418c	\N	auth-username-password-form	Citygroves	8073c234-bfbc-466e-9ab3-84b95fabb6a6	0	10	f	\N	\N
ee14798b-8fab-40da-99f3-91161d6d836f	\N	\N	Citygroves	8073c234-bfbc-466e-9ab3-84b95fabb6a6	1	20	t	4f648c51-6238-4dc0-ac8e-24dcd70b2dd1	\N
0104fe7b-a428-4554-8355-79145745cfef	\N	conditional-user-configured	Citygroves	4f648c51-6238-4dc0-ac8e-24dcd70b2dd1	0	10	f	\N	\N
837749d5-2969-496e-9fb8-f7ce54e6e75e	\N	auth-otp-form	Citygroves	4f648c51-6238-4dc0-ac8e-24dcd70b2dd1	0	20	f	\N	\N
a918c095-f276-48b0-b00c-032efcefc5a0	\N	direct-grant-validate-username	Citygroves	60e1da8c-5e5f-4583-96c4-0be3e745d1a4	0	10	f	\N	\N
c618d50c-0bce-4ca9-b4f9-987d7a24d941	\N	direct-grant-validate-password	Citygroves	60e1da8c-5e5f-4583-96c4-0be3e745d1a4	0	20	f	\N	\N
8ca1d1c1-1851-4fd7-b88e-fad81b474ed4	\N	\N	Citygroves	60e1da8c-5e5f-4583-96c4-0be3e745d1a4	1	30	t	510e8db0-b67e-407d-ab9f-d01029bc5bca	\N
a9b58c12-8f17-491e-8e06-2f0a7fa52f73	\N	conditional-user-configured	Citygroves	510e8db0-b67e-407d-ab9f-d01029bc5bca	0	10	f	\N	\N
bf0fa746-84a8-462d-b144-906fea0e6f81	\N	direct-grant-validate-otp	Citygroves	510e8db0-b67e-407d-ab9f-d01029bc5bca	0	20	f	\N	\N
43b11fb5-3f77-4e62-b059-ec5e072817e2	\N	registration-page-form	Citygroves	e450aca1-68db-4333-8ab0-383861962885	0	10	t	b5375a52-c777-43b5-bb52-514aeb6fc52b	\N
7c03f005-0103-4583-8055-bae6f66d0778	\N	registration-user-creation	Citygroves	b5375a52-c777-43b5-bb52-514aeb6fc52b	0	20	f	\N	\N
48baf7aa-f1cf-4a3f-b288-a75ba8f23e91	\N	registration-profile-action	Citygroves	b5375a52-c777-43b5-bb52-514aeb6fc52b	0	40	f	\N	\N
620d7f05-4529-405d-8720-abb8f3e36453	\N	registration-password-action	Citygroves	b5375a52-c777-43b5-bb52-514aeb6fc52b	0	50	f	\N	\N
fa58486a-ba07-473c-bcc6-4052598df391	\N	registration-recaptcha-action	Citygroves	b5375a52-c777-43b5-bb52-514aeb6fc52b	3	60	f	\N	\N
80f151a7-857a-4d1f-9465-7de554f70d80	\N	reset-credentials-choose-user	Citygroves	e2499a60-4f6d-4a90-99c7-9e95e98e284c	0	10	f	\N	\N
36bf4a71-db36-463d-933e-04ba7ff3d8a5	\N	reset-credential-email	Citygroves	e2499a60-4f6d-4a90-99c7-9e95e98e284c	0	20	f	\N	\N
432dc830-5ca4-4da1-be33-033ac2bdaf8b	\N	reset-password	Citygroves	e2499a60-4f6d-4a90-99c7-9e95e98e284c	0	30	f	\N	\N
6364ca67-48b6-4845-a797-a9b6a1620b3c	\N	\N	Citygroves	e2499a60-4f6d-4a90-99c7-9e95e98e284c	1	40	t	f53bfdde-8464-430e-83d3-ae60f79a893f	\N
17bfe355-903c-4ca6-b062-9b3417ccd3cb	\N	conditional-user-configured	Citygroves	f53bfdde-8464-430e-83d3-ae60f79a893f	0	10	f	\N	\N
a4333674-6b26-47f7-9f30-6d78ca8523fb	\N	reset-otp	Citygroves	f53bfdde-8464-430e-83d3-ae60f79a893f	0	20	f	\N	\N
2a9128c4-da52-4e62-a27a-f4c10892f8f1	\N	client-secret	Citygroves	012ef42e-e757-40ce-8652-09a39e56b7d2	2	10	f	\N	\N
f95abed6-1a37-488f-85d1-bb112c994999	\N	client-jwt	Citygroves	012ef42e-e757-40ce-8652-09a39e56b7d2	2	20	f	\N	\N
6895fde0-25dd-4571-92af-4f7731369431	\N	client-secret-jwt	Citygroves	012ef42e-e757-40ce-8652-09a39e56b7d2	2	30	f	\N	\N
1c61f7fd-f8f5-4d81-b7b9-6f1ea59d21c8	\N	client-x509	Citygroves	012ef42e-e757-40ce-8652-09a39e56b7d2	2	40	f	\N	\N
4456ec30-a333-478b-a614-3c483af9ed4c	\N	idp-review-profile	Citygroves	114dff38-9df0-4c7b-9c0f-e091d7874b34	0	10	f	\N	f8b07a9d-d91c-4ef7-9832-388278b7ffb6
e1e0a584-d3f9-4aeb-8f90-368693103926	\N	\N	Citygroves	114dff38-9df0-4c7b-9c0f-e091d7874b34	0	20	t	b354a413-c1b1-4a73-a7d4-7e8713946e4d	\N
5c8a5bd8-e313-4dab-88a2-38e5b106800e	\N	idp-create-user-if-unique	Citygroves	b354a413-c1b1-4a73-a7d4-7e8713946e4d	2	10	f	\N	08dfbb5a-0021-4fc8-a103-28b6f943bbac
445ecccf-2332-4446-84f5-17ec5b321150	\N	\N	Citygroves	b354a413-c1b1-4a73-a7d4-7e8713946e4d	2	20	t	70466827-2cae-4820-b663-0abf46b40a68	\N
23be4849-5df5-462d-b3de-b2fead88756b	\N	idp-confirm-link	Citygroves	70466827-2cae-4820-b663-0abf46b40a68	0	10	f	\N	\N
ec999952-883c-4196-9755-892fe4f30e0b	\N	\N	Citygroves	70466827-2cae-4820-b663-0abf46b40a68	0	20	t	13bef6d3-7750-40c4-b114-30c17253f156	\N
3f9c1663-69da-44a3-827f-8c7a83fd94bd	\N	idp-email-verification	Citygroves	13bef6d3-7750-40c4-b114-30c17253f156	2	10	f	\N	\N
e5b3cf6a-d9bc-4a2a-b6b4-711473806632	\N	\N	Citygroves	13bef6d3-7750-40c4-b114-30c17253f156	2	20	t	525af5a6-1ea9-40a8-8e9e-01b4c9162627	\N
347d19c8-5eb7-4e39-8677-589483d69e19	\N	idp-username-password-form	Citygroves	525af5a6-1ea9-40a8-8e9e-01b4c9162627	0	10	f	\N	\N
7839ff1d-82c1-43eb-a04f-08e69aef4f58	\N	\N	Citygroves	525af5a6-1ea9-40a8-8e9e-01b4c9162627	1	20	t	f712b13f-b507-4723-a659-3c0f08937ce0	\N
208fee2c-32c0-46ed-860c-3432f3682c79	\N	conditional-user-configured	Citygroves	f712b13f-b507-4723-a659-3c0f08937ce0	0	10	f	\N	\N
0ba0f580-e150-48e2-af8b-0537130a000a	\N	auth-otp-form	Citygroves	f712b13f-b507-4723-a659-3c0f08937ce0	0	20	f	\N	\N
2f0218e4-8925-4eb1-a729-28e1b8451ee2	\N	http-basic-authenticator	Citygroves	9092f1b1-d0bf-47dd-92dd-87a5932bbde8	0	10	f	\N	\N
881ada76-f882-4ac2-8501-b2318807c0fe	\N	docker-http-basic-authenticator	Citygroves	2ab8a208-7817-4084-a6d8-741920490f2e	0	10	f	\N	\N
f4a0e3a3-c97c-4454-86eb-30b99707e7f2	\N	no-cookie-redirect	Citygroves	13248f11-69b2-4308-9af7-98bdb69c2667	0	10	f	\N	\N
c60ae53b-6d47-4058-9e46-db73564cc51b	\N	\N	Citygroves	13248f11-69b2-4308-9af7-98bdb69c2667	0	20	t	53105737-59ec-4b20-a226-c6185f7d8e5c	\N
fcbb8a59-09a6-40ab-a614-faa8cac34da5	\N	basic-auth	Citygroves	53105737-59ec-4b20-a226-c6185f7d8e5c	0	10	f	\N	\N
2d9b3a98-f665-4aa4-a7cf-ab13f2d0c93e	\N	basic-auth-otp	Citygroves	53105737-59ec-4b20-a226-c6185f7d8e5c	3	20	f	\N	\N
f9bce0e8-33a7-4d96-8b7c-a91e1fb15383	\N	auth-spnego	Citygroves	53105737-59ec-4b20-a226-c6185f7d8e5c	3	30	f	\N	\N
\.


--
-- Data for Name: authentication_flow; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authentication_flow (id, alias, description, realm_id, provider_id, top_level, built_in) FROM stdin;
79490408-8ca6-4c72-8065-c1f2979a54ac	browser	browser based authentication	master	basic-flow	t	t
4a14b992-6617-4174-8b52-72e3f8d99578	forms	Username, password, otp and other auth forms.	master	basic-flow	f	t
4789e42a-8381-4575-bea7-85e67898d6f5	Browser - Conditional OTP	Flow to determine if the OTP is required for the authentication	master	basic-flow	f	t
9884d6b5-d7f9-476b-a97f-52d9fb506768	direct grant	OpenID Connect Resource Owner Grant	master	basic-flow	t	t
deee9e90-9891-4ebc-b62d-ce0527845943	Direct Grant - Conditional OTP	Flow to determine if the OTP is required for the authentication	master	basic-flow	f	t
05359703-bbea-467e-a919-d195f5b5175c	registration	registration flow	master	basic-flow	t	t
4cbe71c1-c1f6-4794-96b2-27dfc4fc8e63	registration form	registration form	master	form-flow	f	t
9bf06127-8c95-49e4-a39f-659f818cde5d	reset credentials	Reset credentials for a user if they forgot their password or something	master	basic-flow	t	t
8624d73a-6772-4cf6-9889-7d8f63fad1e7	Reset - Conditional OTP	Flow to determine if the OTP should be reset or not. Set to REQUIRED to force.	master	basic-flow	f	t
b693e22c-d3f3-4c25-8740-5e9e2c4e94db	clients	Base authentication for clients	master	client-flow	t	t
3dd9bc4d-94ce-49d2-8fcb-3e5c5ccab86e	first broker login	Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account	master	basic-flow	t	t
54df3865-4131-4917-a01e-cd964677e365	User creation or linking	Flow for the existing/non-existing user alternatives	master	basic-flow	f	t
bf46b9fe-8c0c-42ea-9297-f92f377f173c	Handle Existing Account	Handle what to do if there is existing account with same email/username like authenticated identity provider	master	basic-flow	f	t
bfaef943-6d4e-4c2b-ac9d-6941584d39f2	Account verification options	Method with which to verity the existing account	master	basic-flow	f	t
20aafc04-3629-40c3-ba8a-7592db17eede	Verify Existing Account by Re-authentication	Reauthentication of existing account	master	basic-flow	f	t
5d306a1b-44c6-4cd3-99db-ab174526f2eb	First broker login - Conditional OTP	Flow to determine if the OTP is required for the authentication	master	basic-flow	f	t
46a57c26-2bb8-4106-adbd-92ded879ff2e	saml ecp	SAML ECP Profile Authentication Flow	master	basic-flow	t	t
4f72d4dd-d825-40a7-91b3-d94247b32937	docker auth	Used by Docker clients to authenticate against the IDP	master	basic-flow	t	t
8e4c4f11-f5bf-412e-8168-68ecf1c73016	http challenge	An authentication flow based on challenge-response HTTP Authentication Schemes	master	basic-flow	t	t
45f0509e-8811-43ee-8c05-adfc9586c916	Authentication Options	Authentication options.	master	basic-flow	f	t
d2818a82-f1db-4276-86fe-246bc5198e12	browser	browser based authentication	Citygroves	basic-flow	t	t
8073c234-bfbc-466e-9ab3-84b95fabb6a6	forms	Username, password, otp and other auth forms.	Citygroves	basic-flow	f	t
4f648c51-6238-4dc0-ac8e-24dcd70b2dd1	Browser - Conditional OTP	Flow to determine if the OTP is required for the authentication	Citygroves	basic-flow	f	t
60e1da8c-5e5f-4583-96c4-0be3e745d1a4	direct grant	OpenID Connect Resource Owner Grant	Citygroves	basic-flow	t	t
510e8db0-b67e-407d-ab9f-d01029bc5bca	Direct Grant - Conditional OTP	Flow to determine if the OTP is required for the authentication	Citygroves	basic-flow	f	t
e450aca1-68db-4333-8ab0-383861962885	registration	registration flow	Citygroves	basic-flow	t	t
b5375a52-c777-43b5-bb52-514aeb6fc52b	registration form	registration form	Citygroves	form-flow	f	t
e2499a60-4f6d-4a90-99c7-9e95e98e284c	reset credentials	Reset credentials for a user if they forgot their password or something	Citygroves	basic-flow	t	t
f53bfdde-8464-430e-83d3-ae60f79a893f	Reset - Conditional OTP	Flow to determine if the OTP should be reset or not. Set to REQUIRED to force.	Citygroves	basic-flow	f	t
012ef42e-e757-40ce-8652-09a39e56b7d2	clients	Base authentication for clients	Citygroves	client-flow	t	t
114dff38-9df0-4c7b-9c0f-e091d7874b34	first broker login	Actions taken after first broker login with identity provider account, which is not yet linked to any Keycloak account	Citygroves	basic-flow	t	t
b354a413-c1b1-4a73-a7d4-7e8713946e4d	User creation or linking	Flow for the existing/non-existing user alternatives	Citygroves	basic-flow	f	t
70466827-2cae-4820-b663-0abf46b40a68	Handle Existing Account	Handle what to do if there is existing account with same email/username like authenticated identity provider	Citygroves	basic-flow	f	t
13bef6d3-7750-40c4-b114-30c17253f156	Account verification options	Method with which to verity the existing account	Citygroves	basic-flow	f	t
525af5a6-1ea9-40a8-8e9e-01b4c9162627	Verify Existing Account by Re-authentication	Reauthentication of existing account	Citygroves	basic-flow	f	t
f712b13f-b507-4723-a659-3c0f08937ce0	First broker login - Conditional OTP	Flow to determine if the OTP is required for the authentication	Citygroves	basic-flow	f	t
9092f1b1-d0bf-47dd-92dd-87a5932bbde8	saml ecp	SAML ECP Profile Authentication Flow	Citygroves	basic-flow	t	t
2ab8a208-7817-4084-a6d8-741920490f2e	docker auth	Used by Docker clients to authenticate against the IDP	Citygroves	basic-flow	t	t
13248f11-69b2-4308-9af7-98bdb69c2667	http challenge	An authentication flow based on challenge-response HTTP Authentication Schemes	Citygroves	basic-flow	t	t
53105737-59ec-4b20-a226-c6185f7d8e5c	Authentication Options	Authentication options.	Citygroves	basic-flow	f	t
\.


--
-- Data for Name: authenticator_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authenticator_config (id, alias, realm_id) FROM stdin;
f39ebfc7-2655-4231-a678-365eb4b8a1a3	review profile config	master
f25bc570-c320-4f6c-a154-a8b9924a141d	create unique user config	master
f8b07a9d-d91c-4ef7-9832-388278b7ffb6	review profile config	Citygroves
08dfbb5a-0021-4fc8-a103-28b6f943bbac	create unique user config	Citygroves
\.


--
-- Data for Name: authenticator_config_entry; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.authenticator_config_entry (authenticator_id, value, name) FROM stdin;
f39ebfc7-2655-4231-a678-365eb4b8a1a3	missing	update.profile.on.first.login
f25bc570-c320-4f6c-a154-a8b9924a141d	false	require.password.update.after.registration
f8b07a9d-d91c-4ef7-9832-388278b7ffb6	missing	update.profile.on.first.login
08dfbb5a-0021-4fc8-a103-28b6f943bbac	false	require.password.update.after.registration
\.


--
-- Data for Name: broker_link; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.broker_link (identity_provider, storage_provider_id, realm_id, broker_user_id, broker_username, token, user_id) FROM stdin;
\.


--
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client (id, enabled, full_scope_allowed, client_id, not_before, public_client, secret, base_url, bearer_only, management_url, surrogate_auth_required, realm_id, protocol, node_rereg_timeout, frontchannel_logout, consent_required, name, service_accounts_enabled, client_authenticator_type, root_url, description, registration_token, standard_flow_enabled, implicit_flow_enabled, direct_access_grants_enabled, always_display_in_console) FROM stdin;
b1f65320-f3da-48ee-9db1-d5b305f1c855	t	t	master-realm	0	f	90ec12fa-9e6b-4aa7-adb5-9641cb95a4a6	\N	t	\N	f	master	\N	0	f	f	master Realm	f	client-secret	\N	\N	\N	t	f	f	f
ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	f	account	0	f	a6371208-b0fe-4aac-a542-065b93392da3	/realms/master/account/	f	\N	f	master	openid-connect	0	f	f	${client_account}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
6855f198-c04b-4086-9ca5-4b21d8d79b83	t	f	account-console	0	t	11ea9646-3c8b-4725-af98-cd39295373ed	/realms/master/account/	f	\N	f	master	openid-connect	0	f	f	${client_account-console}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
e66e1263-40c9-41af-9b09-8a1699959949	t	f	broker	0	f	e581474e-75a4-4359-a454-b45d5ebb116b	\N	f	\N	f	master	openid-connect	0	f	f	${client_broker}	f	client-secret	\N	\N	\N	t	f	f	f
213895bb-cee2-444b-8c09-73ee6428ce92	t	f	security-admin-console	0	t	03d0c16d-068e-4706-ae44-e858847bd927	/admin/master/console/	f	\N	f	master	openid-connect	0	f	f	${client_security-admin-console}	f	client-secret	${authAdminUrl}	\N	\N	t	f	f	f
a5521393-6e82-4687-8c07-6bd39ea385af	t	f	admin-cli	0	t	bce32c3f-b2b2-44bc-b5dd-d2f103c71840	\N	f	\N	f	master	openid-connect	0	f	f	${client_admin-cli}	f	client-secret	\N	\N	\N	f	f	t	f
7551785f-f1ee-4076-9324-786efa9260b7	t	t	Citygroves-realm	0	f	319f6f2d-0718-48ee-9589-cdcd3c2eec84	\N	t	\N	f	master	\N	0	f	f	Citygroves Realm	f	client-secret	\N	\N	\N	t	f	f	f
e08fe2ab-7a6b-4667-b53c-864db2df766a	t	f	realm-management	0	f	f6faa1a8-ed17-4101-b460-42650d494a08	\N	t	\N	f	Citygroves	openid-connect	0	f	f	${client_realm-management}	f	client-secret	\N	\N	\N	t	f	f	f
324d713c-ae08-4f54-8d17-0217a99a1dab	t	f	account	0	f	8c1310cb-4ba2-462a-90e0-b63b0b5bec8a	/realms/Citygroves/account/	f	\N	f	Citygroves	openid-connect	0	f	f	${client_account}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
55b5e24f-bc93-4729-bb0b-849637a9445f	t	f	account-console	0	t	a570330e-f889-4967-97eb-78f2ae166736	/realms/Citygroves/account/	f	\N	f	Citygroves	openid-connect	0	f	f	${client_account-console}	f	client-secret	${authBaseUrl}	\N	\N	t	f	f	f
a5a6a52f-58ff-440a-bc95-690ea7a8871a	t	f	broker	0	f	0fa90ad2-51ed-458c-8369-853b3969024e	\N	f	\N	f	Citygroves	openid-connect	0	f	f	${client_broker}	f	client-secret	\N	\N	\N	t	f	f	f
f35244b5-7de5-4c9f-92ea-b34912e69a8a	t	f	security-admin-console	0	t	14671c10-35b7-4a1c-ab5f-bbd5f2056ada	/admin/Citygroves/console/	f	\N	f	Citygroves	openid-connect	0	f	f	${client_security-admin-console}	f	client-secret	${authAdminUrl}	\N	\N	t	f	f	f
fd90270b-5ae4-4c61-a3b6-2a21f5457254	t	f	admin-cli	0	t	c0a5398e-c146-4c4d-bee0-38c902f50c56	\N	f	\N	f	Citygroves	openid-connect	0	f	f	${client_admin-cli}	f	client-secret	\N	\N	\N	f	f	t	f
5b6ce05b-92ae-458b-a01d-80305bf960df	t	t	citygroves-frontend	0	t	1ec9b671-28a9-4992-8d8e-23505fd7654e	\N	f	http://citygroves.frontend.local/	f	Citygroves	openid-connect	-1	f	f	\N	f	client-secret	http://citygroves.frontend.local/	\N	\N	t	f	t	f
\.


--
-- Data for Name: client_attributes; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_attributes (client_id, value, name) FROM stdin;
6855f198-c04b-4086-9ca5-4b21d8d79b83	S256	pkce.code.challenge.method
213895bb-cee2-444b-8c09-73ee6428ce92	S256	pkce.code.challenge.method
55b5e24f-bc93-4729-bb0b-849637a9445f	S256	pkce.code.challenge.method
f35244b5-7de5-4c9f-92ea-b34912e69a8a	S256	pkce.code.challenge.method
\.


--
-- Data for Name: client_auth_flow_bindings; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_auth_flow_bindings (client_id, flow_id, binding_name) FROM stdin;
\.


--
-- Data for Name: client_default_roles; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_default_roles (client_id, role_id) FROM stdin;
ce09c09e-54bb-4a0a-8b6d-651c069c0361	0e2a4fc9-bc35-4a6f-ac4a-d372f691f5fd
ce09c09e-54bb-4a0a-8b6d-651c069c0361	68b66fea-396d-4885-bda2-974f6ba5b133
324d713c-ae08-4f54-8d17-0217a99a1dab	04776ef2-69dd-432b-8f78-1753011d1569
324d713c-ae08-4f54-8d17-0217a99a1dab	cd62b709-9f11-4d60-b4af-270d69efc371
\.


--
-- Data for Name: client_initial_access; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_initial_access (id, realm_id, "timestamp", expiration, count, remaining_count) FROM stdin;
\.


--
-- Data for Name: client_node_registrations; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_node_registrations (client_id, value, name) FROM stdin;
\.


--
-- Data for Name: client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope (id, name, realm_id, description, protocol) FROM stdin;
f20b7e12-cbf7-4cf2-92e0-ab8245256b83	offline_access	master	OpenID Connect built-in scope: offline_access	openid-connect
952c33c7-6e1a-4166-a2b6-781c4d97c9ad	role_list	master	SAML role list	saml
6fb85823-f6c8-416a-b77d-24f21f73eef3	profile	master	OpenID Connect built-in scope: profile	openid-connect
a1156a4d-3edf-4e46-8802-dc8f7d071c94	email	master	OpenID Connect built-in scope: email	openid-connect
7215e639-b32b-4edc-89fa-109375845473	address	master	OpenID Connect built-in scope: address	openid-connect
af1583de-b675-4dfb-bea4-a3c74d82eaad	phone	master	OpenID Connect built-in scope: phone	openid-connect
1a5c13e3-16a7-46ca-9833-64dbb4541034	roles	master	OpenID Connect scope for add user roles to the access token	openid-connect
1e4543a6-ac19-4298-9722-f555758997f5	web-origins	master	OpenID Connect scope for add allowed web origins to the access token	openid-connect
396a8291-b64d-4f42-8940-14c424b5598c	microprofile-jwt	master	Microprofile - JWT built-in scope	openid-connect
3c8e4d35-bffe-478d-8cb1-36cc46c89663	offline_access	Citygroves	OpenID Connect built-in scope: offline_access	openid-connect
b3d82398-6878-4915-a7f1-99ff0ed9a1c0	role_list	Citygroves	SAML role list	saml
fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	profile	Citygroves	OpenID Connect built-in scope: profile	openid-connect
bcb82f70-fd63-4933-829f-183158674f81	email	Citygroves	OpenID Connect built-in scope: email	openid-connect
c9fbc7ca-d340-460d-abee-9c619f8de40c	address	Citygroves	OpenID Connect built-in scope: address	openid-connect
a72c9669-7fec-43a0-b467-8f2afdc9640d	phone	Citygroves	OpenID Connect built-in scope: phone	openid-connect
0f29d097-c464-4c81-a65d-304a401d1c96	roles	Citygroves	OpenID Connect scope for add user roles to the access token	openid-connect
bb86f232-3c7e-4409-9de7-c0641a261793	web-origins	Citygroves	OpenID Connect scope for add allowed web origins to the access token	openid-connect
9b593dbb-eadb-47ec-badb-bcce9ab0c11f	microprofile-jwt	Citygroves	Microprofile - JWT built-in scope	openid-connect
\.


--
-- Data for Name: client_scope_attributes; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_attributes (scope_id, value, name) FROM stdin;
f20b7e12-cbf7-4cf2-92e0-ab8245256b83	true	display.on.consent.screen
f20b7e12-cbf7-4cf2-92e0-ab8245256b83	${offlineAccessScopeConsentText}	consent.screen.text
952c33c7-6e1a-4166-a2b6-781c4d97c9ad	true	display.on.consent.screen
952c33c7-6e1a-4166-a2b6-781c4d97c9ad	${samlRoleListScopeConsentText}	consent.screen.text
6fb85823-f6c8-416a-b77d-24f21f73eef3	true	display.on.consent.screen
6fb85823-f6c8-416a-b77d-24f21f73eef3	${profileScopeConsentText}	consent.screen.text
6fb85823-f6c8-416a-b77d-24f21f73eef3	true	include.in.token.scope
a1156a4d-3edf-4e46-8802-dc8f7d071c94	true	display.on.consent.screen
a1156a4d-3edf-4e46-8802-dc8f7d071c94	${emailScopeConsentText}	consent.screen.text
a1156a4d-3edf-4e46-8802-dc8f7d071c94	true	include.in.token.scope
7215e639-b32b-4edc-89fa-109375845473	true	display.on.consent.screen
7215e639-b32b-4edc-89fa-109375845473	${addressScopeConsentText}	consent.screen.text
7215e639-b32b-4edc-89fa-109375845473	true	include.in.token.scope
af1583de-b675-4dfb-bea4-a3c74d82eaad	true	display.on.consent.screen
af1583de-b675-4dfb-bea4-a3c74d82eaad	${phoneScopeConsentText}	consent.screen.text
af1583de-b675-4dfb-bea4-a3c74d82eaad	true	include.in.token.scope
1a5c13e3-16a7-46ca-9833-64dbb4541034	true	display.on.consent.screen
1a5c13e3-16a7-46ca-9833-64dbb4541034	${rolesScopeConsentText}	consent.screen.text
1a5c13e3-16a7-46ca-9833-64dbb4541034	false	include.in.token.scope
1e4543a6-ac19-4298-9722-f555758997f5	false	display.on.consent.screen
1e4543a6-ac19-4298-9722-f555758997f5		consent.screen.text
1e4543a6-ac19-4298-9722-f555758997f5	false	include.in.token.scope
396a8291-b64d-4f42-8940-14c424b5598c	false	display.on.consent.screen
396a8291-b64d-4f42-8940-14c424b5598c	true	include.in.token.scope
3c8e4d35-bffe-478d-8cb1-36cc46c89663	true	display.on.consent.screen
3c8e4d35-bffe-478d-8cb1-36cc46c89663	${offlineAccessScopeConsentText}	consent.screen.text
b3d82398-6878-4915-a7f1-99ff0ed9a1c0	true	display.on.consent.screen
b3d82398-6878-4915-a7f1-99ff0ed9a1c0	${samlRoleListScopeConsentText}	consent.screen.text
fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	true	display.on.consent.screen
fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	${profileScopeConsentText}	consent.screen.text
fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	true	include.in.token.scope
bcb82f70-fd63-4933-829f-183158674f81	true	display.on.consent.screen
bcb82f70-fd63-4933-829f-183158674f81	${emailScopeConsentText}	consent.screen.text
bcb82f70-fd63-4933-829f-183158674f81	true	include.in.token.scope
c9fbc7ca-d340-460d-abee-9c619f8de40c	true	display.on.consent.screen
c9fbc7ca-d340-460d-abee-9c619f8de40c	${addressScopeConsentText}	consent.screen.text
c9fbc7ca-d340-460d-abee-9c619f8de40c	true	include.in.token.scope
a72c9669-7fec-43a0-b467-8f2afdc9640d	true	display.on.consent.screen
a72c9669-7fec-43a0-b467-8f2afdc9640d	${phoneScopeConsentText}	consent.screen.text
a72c9669-7fec-43a0-b467-8f2afdc9640d	true	include.in.token.scope
0f29d097-c464-4c81-a65d-304a401d1c96	true	display.on.consent.screen
0f29d097-c464-4c81-a65d-304a401d1c96	${rolesScopeConsentText}	consent.screen.text
0f29d097-c464-4c81-a65d-304a401d1c96	false	include.in.token.scope
bb86f232-3c7e-4409-9de7-c0641a261793	false	display.on.consent.screen
bb86f232-3c7e-4409-9de7-c0641a261793		consent.screen.text
bb86f232-3c7e-4409-9de7-c0641a261793	false	include.in.token.scope
9b593dbb-eadb-47ec-badb-bcce9ab0c11f	false	display.on.consent.screen
9b593dbb-eadb-47ec-badb-bcce9ab0c11f	true	include.in.token.scope
\.


--
-- Data for Name: client_scope_client; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_client (client_id, scope_id, default_scope) FROM stdin;
ce09c09e-54bb-4a0a-8b6d-651c069c0361	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
6855f198-c04b-4086-9ca5-4b21d8d79b83	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
a5521393-6e82-4687-8c07-6bd39ea385af	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
e66e1263-40c9-41af-9b09-8a1699959949	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
b1f65320-f3da-48ee-9db1-d5b305f1c855	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
213895bb-cee2-444b-8c09-73ee6428ce92	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
ce09c09e-54bb-4a0a-8b6d-651c069c0361	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
ce09c09e-54bb-4a0a-8b6d-651c069c0361	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
ce09c09e-54bb-4a0a-8b6d-651c069c0361	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
ce09c09e-54bb-4a0a-8b6d-651c069c0361	1e4543a6-ac19-4298-9722-f555758997f5	t
ce09c09e-54bb-4a0a-8b6d-651c069c0361	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
ce09c09e-54bb-4a0a-8b6d-651c069c0361	7215e639-b32b-4edc-89fa-109375845473	f
ce09c09e-54bb-4a0a-8b6d-651c069c0361	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
ce09c09e-54bb-4a0a-8b6d-651c069c0361	396a8291-b64d-4f42-8940-14c424b5598c	f
6855f198-c04b-4086-9ca5-4b21d8d79b83	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
6855f198-c04b-4086-9ca5-4b21d8d79b83	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
6855f198-c04b-4086-9ca5-4b21d8d79b83	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
6855f198-c04b-4086-9ca5-4b21d8d79b83	1e4543a6-ac19-4298-9722-f555758997f5	t
6855f198-c04b-4086-9ca5-4b21d8d79b83	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
6855f198-c04b-4086-9ca5-4b21d8d79b83	7215e639-b32b-4edc-89fa-109375845473	f
6855f198-c04b-4086-9ca5-4b21d8d79b83	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
6855f198-c04b-4086-9ca5-4b21d8d79b83	396a8291-b64d-4f42-8940-14c424b5598c	f
a5521393-6e82-4687-8c07-6bd39ea385af	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
a5521393-6e82-4687-8c07-6bd39ea385af	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
a5521393-6e82-4687-8c07-6bd39ea385af	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
a5521393-6e82-4687-8c07-6bd39ea385af	1e4543a6-ac19-4298-9722-f555758997f5	t
a5521393-6e82-4687-8c07-6bd39ea385af	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
a5521393-6e82-4687-8c07-6bd39ea385af	7215e639-b32b-4edc-89fa-109375845473	f
a5521393-6e82-4687-8c07-6bd39ea385af	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
a5521393-6e82-4687-8c07-6bd39ea385af	396a8291-b64d-4f42-8940-14c424b5598c	f
e66e1263-40c9-41af-9b09-8a1699959949	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
e66e1263-40c9-41af-9b09-8a1699959949	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
e66e1263-40c9-41af-9b09-8a1699959949	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
e66e1263-40c9-41af-9b09-8a1699959949	1e4543a6-ac19-4298-9722-f555758997f5	t
e66e1263-40c9-41af-9b09-8a1699959949	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
e66e1263-40c9-41af-9b09-8a1699959949	7215e639-b32b-4edc-89fa-109375845473	f
e66e1263-40c9-41af-9b09-8a1699959949	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
e66e1263-40c9-41af-9b09-8a1699959949	396a8291-b64d-4f42-8940-14c424b5598c	f
b1f65320-f3da-48ee-9db1-d5b305f1c855	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
b1f65320-f3da-48ee-9db1-d5b305f1c855	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
b1f65320-f3da-48ee-9db1-d5b305f1c855	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
b1f65320-f3da-48ee-9db1-d5b305f1c855	1e4543a6-ac19-4298-9722-f555758997f5	t
b1f65320-f3da-48ee-9db1-d5b305f1c855	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
b1f65320-f3da-48ee-9db1-d5b305f1c855	7215e639-b32b-4edc-89fa-109375845473	f
b1f65320-f3da-48ee-9db1-d5b305f1c855	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
b1f65320-f3da-48ee-9db1-d5b305f1c855	396a8291-b64d-4f42-8940-14c424b5598c	f
213895bb-cee2-444b-8c09-73ee6428ce92	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
213895bb-cee2-444b-8c09-73ee6428ce92	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
213895bb-cee2-444b-8c09-73ee6428ce92	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
213895bb-cee2-444b-8c09-73ee6428ce92	1e4543a6-ac19-4298-9722-f555758997f5	t
213895bb-cee2-444b-8c09-73ee6428ce92	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
213895bb-cee2-444b-8c09-73ee6428ce92	7215e639-b32b-4edc-89fa-109375845473	f
213895bb-cee2-444b-8c09-73ee6428ce92	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
213895bb-cee2-444b-8c09-73ee6428ce92	396a8291-b64d-4f42-8940-14c424b5598c	f
7551785f-f1ee-4076-9324-786efa9260b7	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
7551785f-f1ee-4076-9324-786efa9260b7	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
7551785f-f1ee-4076-9324-786efa9260b7	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
7551785f-f1ee-4076-9324-786efa9260b7	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
7551785f-f1ee-4076-9324-786efa9260b7	1e4543a6-ac19-4298-9722-f555758997f5	t
7551785f-f1ee-4076-9324-786efa9260b7	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
7551785f-f1ee-4076-9324-786efa9260b7	7215e639-b32b-4edc-89fa-109375845473	f
7551785f-f1ee-4076-9324-786efa9260b7	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
7551785f-f1ee-4076-9324-786efa9260b7	396a8291-b64d-4f42-8940-14c424b5598c	f
324d713c-ae08-4f54-8d17-0217a99a1dab	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
55b5e24f-bc93-4729-bb0b-849637a9445f	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
fd90270b-5ae4-4c61-a3b6-2a21f5457254	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
a5a6a52f-58ff-440a-bc95-690ea7a8871a	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
e08fe2ab-7a6b-4667-b53c-864db2df766a	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
f35244b5-7de5-4c9f-92ea-b34912e69a8a	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
324d713c-ae08-4f54-8d17-0217a99a1dab	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
324d713c-ae08-4f54-8d17-0217a99a1dab	bcb82f70-fd63-4933-829f-183158674f81	t
324d713c-ae08-4f54-8d17-0217a99a1dab	0f29d097-c464-4c81-a65d-304a401d1c96	t
324d713c-ae08-4f54-8d17-0217a99a1dab	bb86f232-3c7e-4409-9de7-c0641a261793	t
324d713c-ae08-4f54-8d17-0217a99a1dab	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
324d713c-ae08-4f54-8d17-0217a99a1dab	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
324d713c-ae08-4f54-8d17-0217a99a1dab	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
324d713c-ae08-4f54-8d17-0217a99a1dab	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
55b5e24f-bc93-4729-bb0b-849637a9445f	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
55b5e24f-bc93-4729-bb0b-849637a9445f	bcb82f70-fd63-4933-829f-183158674f81	t
55b5e24f-bc93-4729-bb0b-849637a9445f	0f29d097-c464-4c81-a65d-304a401d1c96	t
55b5e24f-bc93-4729-bb0b-849637a9445f	bb86f232-3c7e-4409-9de7-c0641a261793	t
55b5e24f-bc93-4729-bb0b-849637a9445f	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
55b5e24f-bc93-4729-bb0b-849637a9445f	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
55b5e24f-bc93-4729-bb0b-849637a9445f	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
55b5e24f-bc93-4729-bb0b-849637a9445f	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
fd90270b-5ae4-4c61-a3b6-2a21f5457254	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
fd90270b-5ae4-4c61-a3b6-2a21f5457254	bcb82f70-fd63-4933-829f-183158674f81	t
fd90270b-5ae4-4c61-a3b6-2a21f5457254	0f29d097-c464-4c81-a65d-304a401d1c96	t
fd90270b-5ae4-4c61-a3b6-2a21f5457254	bb86f232-3c7e-4409-9de7-c0641a261793	t
fd90270b-5ae4-4c61-a3b6-2a21f5457254	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
fd90270b-5ae4-4c61-a3b6-2a21f5457254	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
fd90270b-5ae4-4c61-a3b6-2a21f5457254	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
fd90270b-5ae4-4c61-a3b6-2a21f5457254	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
a5a6a52f-58ff-440a-bc95-690ea7a8871a	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
a5a6a52f-58ff-440a-bc95-690ea7a8871a	bcb82f70-fd63-4933-829f-183158674f81	t
a5a6a52f-58ff-440a-bc95-690ea7a8871a	0f29d097-c464-4c81-a65d-304a401d1c96	t
a5a6a52f-58ff-440a-bc95-690ea7a8871a	bb86f232-3c7e-4409-9de7-c0641a261793	t
a5a6a52f-58ff-440a-bc95-690ea7a8871a	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
a5a6a52f-58ff-440a-bc95-690ea7a8871a	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
a5a6a52f-58ff-440a-bc95-690ea7a8871a	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
a5a6a52f-58ff-440a-bc95-690ea7a8871a	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
e08fe2ab-7a6b-4667-b53c-864db2df766a	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
e08fe2ab-7a6b-4667-b53c-864db2df766a	bcb82f70-fd63-4933-829f-183158674f81	t
e08fe2ab-7a6b-4667-b53c-864db2df766a	0f29d097-c464-4c81-a65d-304a401d1c96	t
e08fe2ab-7a6b-4667-b53c-864db2df766a	bb86f232-3c7e-4409-9de7-c0641a261793	t
e08fe2ab-7a6b-4667-b53c-864db2df766a	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
e08fe2ab-7a6b-4667-b53c-864db2df766a	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
e08fe2ab-7a6b-4667-b53c-864db2df766a	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
e08fe2ab-7a6b-4667-b53c-864db2df766a	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
f35244b5-7de5-4c9f-92ea-b34912e69a8a	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
f35244b5-7de5-4c9f-92ea-b34912e69a8a	bcb82f70-fd63-4933-829f-183158674f81	t
f35244b5-7de5-4c9f-92ea-b34912e69a8a	0f29d097-c464-4c81-a65d-304a401d1c96	t
f35244b5-7de5-4c9f-92ea-b34912e69a8a	bb86f232-3c7e-4409-9de7-c0641a261793	t
f35244b5-7de5-4c9f-92ea-b34912e69a8a	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
f35244b5-7de5-4c9f-92ea-b34912e69a8a	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
f35244b5-7de5-4c9f-92ea-b34912e69a8a	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
f35244b5-7de5-4c9f-92ea-b34912e69a8a	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
5b6ce05b-92ae-458b-a01d-80305bf960df	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
5b6ce05b-92ae-458b-a01d-80305bf960df	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
5b6ce05b-92ae-458b-a01d-80305bf960df	bcb82f70-fd63-4933-829f-183158674f81	t
5b6ce05b-92ae-458b-a01d-80305bf960df	0f29d097-c464-4c81-a65d-304a401d1c96	t
5b6ce05b-92ae-458b-a01d-80305bf960df	bb86f232-3c7e-4409-9de7-c0641a261793	t
5b6ce05b-92ae-458b-a01d-80305bf960df	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
5b6ce05b-92ae-458b-a01d-80305bf960df	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
5b6ce05b-92ae-458b-a01d-80305bf960df	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
5b6ce05b-92ae-458b-a01d-80305bf960df	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
\.


--
-- Data for Name: client_scope_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_scope_role_mapping (scope_id, role_id) FROM stdin;
f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f6c96cdc-4f19-4bde-bea5-6edef4d84f7a
3c8e4d35-bffe-478d-8cb1-36cc46c89663	70324447-9abb-449c-8d07-4bb22b9643b7
\.


--
-- Data for Name: client_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session (id, client_id, redirect_uri, state, "timestamp", session_id, auth_method, realm_id, auth_user_id, current_action) FROM stdin;
\.


--
-- Data for Name: client_session_auth_status; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_auth_status (authenticator, status, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_note (name, value, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_prot_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_prot_mapper (protocol_mapper_id, client_session) FROM stdin;
\.


--
-- Data for Name: client_session_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_session_role (role_id, client_session) FROM stdin;
\.


--
-- Data for Name: client_user_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.client_user_session_note (name, value, client_session) FROM stdin;
\.


--
-- Data for Name: component; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.component (id, name, parent_id, provider_id, provider_type, realm_id, sub_type) FROM stdin;
6bb93ef6-43f7-4921-b965-7ecffdac45b0	Trusted Hosts	master	trusted-hosts	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
bbcac7d1-1d44-4044-a317-3baa267ce95c	Consent Required	master	consent-required	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
31b58fe4-f8b1-48e6-bf3f-dd3465518917	Full Scope Disabled	master	scope	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
05a7d332-db20-4ab3-b574-faa22ec52ed9	Max Clients Limit	master	max-clients	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
c9d4370b-c413-47fe-afc2-46d76a84b894	Allowed Protocol Mapper Types	master	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
ec228a4e-2da2-4537-af52-af4fde8c1b7e	Allowed Client Scopes	master	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	anonymous
ca5afee1-61e7-4469-ad32-db51ffaeb6d1	Allowed Protocol Mapper Types	master	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	authenticated
9db2bced-bbba-447d-882e-4a6a80ad8242	Allowed Client Scopes	master	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	master	authenticated
e2221400-532f-41a0-88a0-516c52ee6d06	rsa-generated	master	rsa-generated	org.keycloak.keys.KeyProvider	master	\N
29196384-5aa7-40e7-af45-686ea58fd295	hmac-generated	master	hmac-generated	org.keycloak.keys.KeyProvider	master	\N
6fd97428-001b-47e7-b96e-501703633079	aes-generated	master	aes-generated	org.keycloak.keys.KeyProvider	master	\N
282454e7-8b06-4b99-8481-98450821098e	rsa-generated	Citygroves	rsa-generated	org.keycloak.keys.KeyProvider	Citygroves	\N
13fb7f43-2078-4878-867b-407c9c53c5ec	hmac-generated	Citygroves	hmac-generated	org.keycloak.keys.KeyProvider	Citygroves	\N
3532a2f6-0b3e-49b5-a28d-539474f02310	aes-generated	Citygroves	aes-generated	org.keycloak.keys.KeyProvider	Citygroves	\N
b0a6f9dd-e922-40e4-ae06-c7981eec65b0	Trusted Hosts	Citygroves	trusted-hosts	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
9951aef7-79c6-49d8-b201-050340b7acf0	Consent Required	Citygroves	consent-required	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
233d49f5-7597-4c51-81c2-602dc8c7e80c	Full Scope Disabled	Citygroves	scope	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
6f26cac5-ebb1-46e4-9d2d-dd12b366ce60	Max Clients Limit	Citygroves	max-clients	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	Allowed Protocol Mapper Types	Citygroves	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
dd5ea82b-c647-4aa9-ae16-fc21f07a0720	Allowed Client Scopes	Citygroves	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	anonymous
338b2332-f6a8-4407-a9d3-fbdc120950da	Allowed Protocol Mapper Types	Citygroves	allowed-protocol-mappers	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	authenticated
79be782c-66ab-42e3-a0fb-ed7275ad13cf	Allowed Client Scopes	Citygroves	allowed-client-templates	org.keycloak.services.clientregistration.policy.ClientRegistrationPolicy	Citygroves	authenticated
\.


--
-- Data for Name: component_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.component_config (id, component_id, name, value) FROM stdin;
0b04d801-ef18-433b-a84b-69f3bd4099f8	9db2bced-bbba-447d-882e-4a6a80ad8242	allow-default-scopes	true
7c74bb10-fb77-43b6-8bb7-cf9525405f36	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
536903a0-41e7-431f-a22b-2a33e153ffc8	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
8fac7c58-505a-475a-9674-2bb8fd5b40f3	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	saml-role-list-mapper
ee388e7f-5391-447f-82a7-9625624553d2	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	saml-user-property-mapper
708f708f-080d-4639-bb91-cc2a93ad0eda	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
24025c83-4e86-43c1-80c3-503d011310ba	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	oidc-address-mapper
9c53448a-0f88-4709-a575-8e74cdc91d5c	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	saml-user-attribute-mapper
8800bc4d-13af-4fa8-899b-79ac77ace14f	ca5afee1-61e7-4469-ad32-db51ffaeb6d1	allowed-protocol-mapper-types	oidc-full-name-mapper
3e2ec92c-3510-4d06-85ba-d506d0da56a9	6bb93ef6-43f7-4921-b965-7ecffdac45b0	client-uris-must-match	true
611278c8-c610-416d-aa44-6d2c4a9d965b	6bb93ef6-43f7-4921-b965-7ecffdac45b0	host-sending-registration-request-must-match	true
7e0d4ba2-a2ec-4d07-90fa-4223efa2885d	05a7d332-db20-4ab3-b574-faa22ec52ed9	max-clients	200
d593de73-6aec-4b09-a074-4ed934d013b7	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
6425aeb5-dc24-44a8-8211-58a911adacc5	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
92ecc5a8-9acc-4b40-b318-701fc1de60dd	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	oidc-full-name-mapper
935b8084-0b04-41c7-9af5-75a5ea36893e	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	saml-user-property-mapper
97efefe3-6913-480c-818f-2150c0964dac	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
d5d8a30f-ee4c-4d4c-950c-c74a50856a95	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	saml-user-attribute-mapper
bfe31661-ff9c-4db1-b33c-1815b97c5f98	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	oidc-address-mapper
45cf561a-c4fb-42f7-aa51-7040d27854e7	c9d4370b-c413-47fe-afc2-46d76a84b894	allowed-protocol-mapper-types	saml-role-list-mapper
309f18ef-abd7-4dbc-ae67-ac1a4aeed794	ec228a4e-2da2-4537-af52-af4fde8c1b7e	allow-default-scopes	true
1ed07be6-196d-48ad-acd0-91eea9271dc6	e2221400-532f-41a0-88a0-516c52ee6d06	certificate	MIICmzCCAYMCBgFxOF+JXjANBgkqhkiG9w0BAQsFADARMQ8wDQYDVQQDDAZtYXN0ZXIwHhcNMjAwNDAyMDA1MDE3WhcNMzAwNDAyMDA1MTU3WjARMQ8wDQYDVQQDDAZtYXN0ZXIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC1DfU/YSpwL+F3w2iOXIfVf7bNL/AWjUBi69sNFs4hkzuqKoC24rDTelvjYI4VV/spgvjla9k6l4zk1VDh55Rl+u5mT9aTmtJyV+K7Oq0UmBQUYkfMusvyeLrv83c/V4IgJE8ZHXmSVd7uEWnfEhkSNxcX7b0c2yTbKMmKTCc01tarnGXB91ckGVqSJG6Kk4XXW8RcUe4Rd6vh00x+vYwNWu+qAp4VfV51PO+Pk7dvNgVOX3DY7VuSqI0eAaVJpNgnEfqXlKEEKr54KN2wf2UZXYafwuS5h6vi1QB9egXKqzA0YYPKBpKYPReskZ53eF/9Zui3V3SlTl88g68sIavrAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAHB23rNaHTIC2yYWoAGy+CHUMsPs+3omKKrDL8xmesNWU9swEgZ3qqIhFDi2QED/uuD4s16u32mPEJcV5OZ6IbfEHKOJY0jEhfKfNepCQZjApn0B0Ds7nsCvo8N7/+LAk4wuK7mTxOn8YGntzlGz36Ls2E7wLSxYde6m2wV6V6TKwGVqbCRo64WUsGW5FezNGy/p/zakLB0q6hMRc1woJRBanH2K84wyN6lYH7FCwFIUOFv/Pycq6rZM2Z0cEcidlSvu/7t7D9Cu8lTZmcCDPHcXjLfC3eODuDBwSFFBXeVPVrEpCLR5QAahV5HS1ysFBMb6SIKiYzkvFaCuFaX5N+Q=
b5ec6f3a-ab06-4ea9-bc20-152825fcd119	e2221400-532f-41a0-88a0-516c52ee6d06	priority	100
14e5944a-7192-4b68-8cd9-977232202eb8	e2221400-532f-41a0-88a0-516c52ee6d06	privateKey	MIIEpQIBAAKCAQEAtQ31P2EqcC/hd8NojlyH1X+2zS/wFo1AYuvbDRbOIZM7qiqAtuKw03pb42COFVf7KYL45WvZOpeM5NVQ4eeUZfruZk/Wk5rSclfiuzqtFJgUFGJHzLrL8ni67/N3P1eCICRPGR15klXe7hFp3xIZEjcXF+29HNsk2yjJikwnNNbWq5xlwfdXJBlakiRuipOF11vEXFHuEXer4dNMfr2MDVrvqgKeFX1edTzvj5O3bzYFTl9w2O1bkqiNHgGlSaTYJxH6l5ShBCq+eCjdsH9lGV2Gn8LkuYer4tUAfXoFyqswNGGDygaSmD0XrJGed3hf/Wbot1d0pU5fPIOvLCGr6wIDAQABAoIBAByS6lypUhBIjjXfghXNpqZcNJZndWWpvzqdbIHBUqDb4rO1Z4D1f+CwU+Yrq+DUdNAVWoCip7LmjhbjT5OHf9UkaBF/kibTbVkcY60W0pAIfErHQ/uck2leAmqyKuS1Q9Ucxdr52uDsanV6DBJngcttJFjjbVAricKIyl3oLNvatBqwPg0DOJ1LBOjNjxugp6gozbnuDPLuLtZRSlYDpeYOgguZSYEgsyUiepM47WZG7e3Wz4t/vpBnXBjbyQzsKDyp/Ww8bWfKINW1kOtwSYGTtP8KMO3LBVNUuzc54Dt3UWAZyXSA4oBefLcBUj9z/rYLbPTZtfa2L9XOcyxW/1kCgYEA4R0rgf29ql93nulqBlgcsZf7O3PswvwPC1WuZ7O884092rs4MaENkeZJt4zeGeYHwXk8+u/bDKSX/GGF70OMKwJvN4tJ8kBMeBZ4ExgfmHJy7RaMuTCB0YRi32GlJp+gFT3531KzMXDOo5FIx/borbK7MtcAeTIPU20pGofW6YcCgYEAzeVCUJDV3PhrhfQoYMq9Cm6j4py2R8uZC8GtbdT6NkuuSyjfiKLQqvmvlNWZwUvKPazfASbxI+8IKZGLCL+/sUGWwWiqk7tKi5brjz36cf4I59Rs5TfKi+yW8gIv62L96ry0xxXsBOA5FpXAdBKpIu7EScgd4tyoP8/kLBLmc30CgYEAqmYyMMupbfWlzpxQrUy1K5knivFNHqs9mA7bXZQoSxN25sMg3jBS3UW8NzxiQqhk5oanKiu1W/SbN2d6wooW59eH6Dt/Vehl+eDIM2vnPrYjWGPhUazuF3JmhUCciof53Rp0sh8flSUWxamLthGoPxMzsGAe8555C2Vt369DdrECgYEAhQJCmctG7S3qQCnfX8/42WFqK72zH6ROJUMj51z7mtG/Mbyg0yLjDGCqZcqrPizY5Ijls1fV1bHYIwprt+YvTrIhUqZr8229lXmUiP+v564FUMZw5o7pIQVg6cwx6q0TfW4Ulrv5sZisKIPrRNC9RNzcHxHRBLopUrfZHgPDrf0CgYEAzcdYHPyURt5Ldaoc9PheAlmVTq8bbRO5W9KrB0Lysw44skzGLFyZj8ILKlGJQ59e6k9zswG0tjprPvuxHmWPw/EmLxQdCmsuJr1Rn5WN9f5EWrD+mHUAe8Cvl4jYM3+LoAf87b/5hMX4dKMz4ZCwxkFFHNoPU6IB3Dzn3/xNIGQ=
b17b994f-9137-4eb9-9a3f-0bd60055e06c	6fd97428-001b-47e7-b96e-501703633079	secret	tgvYNQHEkZ0b54mkhdSpdA
aba98974-3e7f-4c9a-9e3d-2e55aefd73db	6fd97428-001b-47e7-b96e-501703633079	priority	100
6138ee29-f8f2-4bb6-ab62-8d5eb9933bae	6fd97428-001b-47e7-b96e-501703633079	kid	13594030-c643-41d6-9b61-12cd5cb43e41
486a30ea-0863-4fff-a6c3-5eb3bb296cc5	29196384-5aa7-40e7-af45-686ea58fd295	priority	100
50d1e26c-6003-4280-823a-c1d9fac29a1d	29196384-5aa7-40e7-af45-686ea58fd295	kid	f9aa8ddd-236f-45e4-9d75-8e1d7afbe966
af1f3f9f-05d2-4f9a-a3b8-d6833ff6bb35	29196384-5aa7-40e7-af45-686ea58fd295	algorithm	HS256
6a1acc60-6c5b-406a-9ce3-9a9ee955f52e	29196384-5aa7-40e7-af45-686ea58fd295	secret	VGizegcdgZY-0H22aOOdEpsgW6HGM7yq97sidSp9vG1ThwxjUzsmdUoghT3PT9WaUAmt5ZGNz0B1pVqh7VFNSQ
9e181dcc-b62f-4527-b9f8-618f484dcd56	3532a2f6-0b3e-49b5-a28d-539474f02310	priority	100
13cffd48-ddd7-4ed0-81ab-e146777f0f2d	3532a2f6-0b3e-49b5-a28d-539474f02310	secret	IH4ixJ-CvZ2jk2IVpZJOkA
0e921f2d-3dfc-4432-81ca-9fbbdefca364	3532a2f6-0b3e-49b5-a28d-539474f02310	kid	e167a8f9-d8b1-4afc-918e-1535a0aaab8c
b77840e6-46f8-4c78-b0bd-d6dab1f8a1c4	13fb7f43-2078-4878-867b-407c9c53c5ec	secret	PS3u_fp_BoU3gcRU7DmRwvJ6q-GY69H6cK7xS0yKbFASrLRcW9Md9ASdEVie01T9nz0MYxPMHjg6fnWzDMfzqg
28979447-a6fd-4cc8-9095-c4164a6677c6	13fb7f43-2078-4878-867b-407c9c53c5ec	priority	100
caca86e3-7106-46b7-a72d-0cb48cdadf2d	13fb7f43-2078-4878-867b-407c9c53c5ec	algorithm	HS256
d7a5287f-cf50-4f57-970a-93f50be9f323	13fb7f43-2078-4878-867b-407c9c53c5ec	kid	c784c05b-fdd6-4ba1-8f87-840a0649ac42
5fd8b128-0407-4a25-9652-327722248ebb	282454e7-8b06-4b99-8481-98450821098e	priority	100
237e4391-dfea-4ed4-8448-64222f07512d	282454e7-8b06-4b99-8481-98450821098e	certificate	MIICozCCAYsCBgFxO8DeKjANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDDApDaXR5Z3JvdmVzMB4XDTIwMDQwMjE2MzUyN1oXDTMwMDQwMjE2MzcwN1owFTETMBEGA1UEAwwKQ2l0eWdyb3ZlczCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJacsTu3Ih5HX6dOIAFUg+VLbF5u7yQhVZ6ti+QQl2CyaABijNmjbG1qBqKWqa0L6CkmG1TV4CQlLZnlPDNKUqQDM1e8ixkOOOk+hmHhjWFw6AaFh29iM04OKmXsFWmB5ByMFNSzbgGDWrBBy7+kQLalaI82U0edxLMSaahYlUCMzH8byqzrha+pt0C0nuCKXXUsxWAAAowdvSXVbtl23oI9jq8wI4bT6B1cjZgRbb8feGecIfv7+dfM94Db0PVTkYLVDyL62cjNhY/SxU4wfBucG8AKfoj3fOM1JwdbkjHzzgRtcSCw7OUqZkxb42f2xjxLJsJZuDldGMjeF1Wo0GsCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEABYdnmwld6E+fTPXfCXqi2zZ+g+4dxV51S0uR+OD/IaD5lzfCTQ6D2hW5I4NIpiV/M3hFqfoFWTNznKtRgZo3jzPG+5tFmZQkPqeJ28haAiSgiPr00x0vafQQipPdf7rDMOvzzNkJo+EhPGcZSCP3KsSklAPqnmrn+X3AT9ina6nuXyeyeLbQ2zwk3YouLiprIy7p5CxAMWBNtZgoaEmmTz2VnHrdcPpofCsLyycsEyZ+QDThjUplwK7r2qwgE3GcxZw0H4AhM8+YQsifc1HdHCnwJFCUoCOJmPpYiqBQWUFBIwJColtNF/dGwpE+noLetOqVSz3Gnqf6Mij4OL5iRA==
97a42cbf-edb8-453d-b654-b209ba948df5	282454e7-8b06-4b99-8481-98450821098e	privateKey	MIIEogIBAAKCAQEAlpyxO7ciHkdfp04gAVSD5UtsXm7vJCFVnq2L5BCXYLJoAGKM2aNsbWoGopaprQvoKSYbVNXgJCUtmeU8M0pSpAMzV7yLGQ446T6GYeGNYXDoBoWHb2IzTg4qZewVaYHkHIwU1LNuAYNasEHLv6RAtqVojzZTR53EsxJpqFiVQIzMfxvKrOuFr6m3QLSe4IpddSzFYAACjB29JdVu2Xbegj2OrzAjhtPoHVyNmBFtvx94Z5wh+/v518z3gNvQ9VORgtUPIvrZyM2Fj9LFTjB8G5wbwAp+iPd84zUnB1uSMfPOBG1xILDs5SpmTFvjZ/bGPEsmwlm4OV0YyN4XVajQawIDAQABAoIBACrHkRPsHZXKIiJMb4zRK7GabcqY6fYyPbaXhs+d4tGFe0L4uxcqcybU4dOWxdUwN55Qg5ziLws1QDGhSisrZjPN8Oxv0naocoPVzafJwDW4Mz9++AwsMXRvU52lpCNW0KtHIreTy6BEZiMAXVYu2m7Gpt9ex+LkrjVK+pXlq2cs5SbHV6GVmLRnZIV7r7xSV8UzrBpcGQTRroL99kGUaWL8sabmCJZI3anr1JDcBfWqCXgT2K/vWQb8Je1necr0nF/5k6LtHYMTZlkuUdllPfx6rYtu3qSaNi6MzrS/ZV3IcIT68m/zLrQE45EGzTbLRBO+lqwcvjF9ZA+Nz5B4RYECgYEA8F3qPRa/Q1qDOapaRNV1Tb6kKjSrdBLXjWGd6h0zc+rI9Qj+d/6E0aFxUP5PU9ufIYCnwyMKWpgA6ccwx8qG2sG6Ilk5fvANw2+z9vVlxCMdJGikZkZPhvQbvdNbm+lb416OVZ3FNKBSadwrebh94Bzee401P8EHgqgLyBWMo6sCgYEAoGhecuh2vOTARTfYC5KAJlB8Lv4qMbARUWjB2Zf9PRRhdj4UTVaWhKu6oRRdtiIoNmrj6YPwqPCmX5XdfY+nYq2a4dWV8kjxIxzhHNJY/sWIzHzQMW83OM0ahXhnE1qD8atrycveVGyQ622AmXd3UbUN/esYFtpIxoJ+EyYXxkECgYB0BcEVL6+uwTfqU9Iyu55dopH3VWkVJCsrsVzaLrIxV7kcnfTG0vIlhfn+kGKWJcKQF1vjEzziMdDvBxkCtz2UxkIkZlEcdp8OIRMLN7Shkhl1A5WnUHT+vUHOxQDJJ0EVZQTrSrZwCpr9QisyG92WmhjCJoz3cyM+7AKT1+ME9QKBgCOHeoQRIVutfzjVqbDGfkP+R8NQ4J+o0+0oOuerVpgUz5GVJoIKz8QLFYdgL3GMF0QWYOz0IHYK947sbubEztp4gXnMCS5lIaQZXXM41CV6M1a3vpV0gNK/+0Pc61fKELeStIk58sDYWzEKTBWx9GfQpoy7adaF+uCdPreXFGUBAoGAAXJi67PFl9U3tYQHcS78zRGi0Nwx16ZO2JuC5R5DqlriYcaHXcPw59b5nKuQea6xoMNayG5KuwjJMWNbnfMWD27j8PKnGBclpGgOQP0YHGTiBUaxHXJiVmAdzGoWmSsNO8dUYTN511Y817iZeyJptO8UtgcBJR//EyOZcLTzDtE=
697899cb-39c5-445a-863c-2d044be5f993	dd5ea82b-c647-4aa9-ae16-fc21f07a0720	allow-default-scopes	true
eda4692d-c3bf-40be-8f0c-98a248f6f1e0	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
76d4ad0b-cd93-48f9-9228-f67731f1c3af	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	saml-role-list-mapper
42ea6043-12a9-4331-8e19-5269f356c315	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
10bd7748-33d8-4081-8908-f74bc0204cd2	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	saml-user-property-mapper
f9c5f75f-ebb2-4f13-9fd5-f9ba968ef1d0	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	oidc-full-name-mapper
0660be4c-ae54-4870-a95c-4b06ec88cb1b	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	saml-user-attribute-mapper
13302a68-6b65-4383-a8b6-98acc0dc4efe	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
fe4ce146-187b-41a0-81f6-2cc4607804d0	338b2332-f6a8-4407-a9d3-fbdc120950da	allowed-protocol-mapper-types	oidc-address-mapper
30e98b02-b827-4b16-94fd-41f654fcb98e	6f26cac5-ebb1-46e4-9d2d-dd12b366ce60	max-clients	200
0c4bcf45-d5de-4f0a-913c-bd4bafd33eaf	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	saml-user-attribute-mapper
525f4932-0503-4a9e-bf36-81850a6b271d	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	oidc-usermodel-attribute-mapper
26df9c24-15cb-4c74-a5af-2354e3b48b22	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	oidc-full-name-mapper
94cf7f77-6ec3-4707-bfef-f98d3dce7f29	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	saml-role-list-mapper
8e0afc6d-48e9-448c-bc79-2a2da328057d	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	saml-user-property-mapper
0edf9ad7-818f-449d-80ec-f43119a4a4d5	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	oidc-address-mapper
b856cba7-4648-478f-9463-0dde77ee0121	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	oidc-sha256-pairwise-sub-mapper
fc02c30d-5ec7-4a9e-b615-a7769794b08c	bd4a1c96-9d34-4b95-a68b-a332c78b6b7e	allowed-protocol-mapper-types	oidc-usermodel-property-mapper
43e62685-a47a-4576-964f-5ee6cda066cd	b0a6f9dd-e922-40e4-ae06-c7981eec65b0	host-sending-registration-request-must-match	true
481ee184-4867-4eec-8a01-58ca9a9427c2	b0a6f9dd-e922-40e4-ae06-c7981eec65b0	client-uris-must-match	true
c963d036-d13b-4304-97b1-1a871049ac3b	79be782c-66ab-42e3-a0fb-ed7275ad13cf	allow-default-scopes	true
\.


--
-- Data for Name: composite_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.composite_role (composite, child_role) FROM stdin;
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	23a20ea9-7cd4-4dd9-bd24-38011be8b322
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	76a96647-e367-42cf-8c70-5fc5ad5e1da0
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	065ac91d-c450-4dcb-ac2f-0edadfd26a08
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	4e857f49-5487-4191-af86-2b7b7b3f2e1a
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	b556fb9e-09c4-4b91-86dd-916afa75c911
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	f78ac3ef-5e25-4925-8fc8-69c1135a8543
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	e169fa79-ed79-4090-9535-c7e8099ce26b
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	01f89448-3b46-4a8a-b8b2-1cd291fb185a
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	02bef763-579f-4fc2-826f-f62198dba9ce
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	bd868368-8c11-4196-b88a-20c17dcbd4c5
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	1a051660-cf53-414e-bcee-a4bb4b792466
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	90a63da7-d46d-4732-a5e6-5f7f4ba53061
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	c80801d4-b6d0-445b-a8d6-2fb498792963
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	ba9db82c-8285-48bd-950e-99865b6874eb
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	27abfef1-64d5-44ea-b1d5-63154e3a9d16
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	3f3f7ecd-9c78-45e2-91d8-f5aea758f6ac
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	b50cfdd3-41b5-43cd-b008-1d6b07e4b8ba
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	44a86e3c-9b8f-4331-801b-b88030479bce
4e857f49-5487-4191-af86-2b7b7b3f2e1a	27abfef1-64d5-44ea-b1d5-63154e3a9d16
4e857f49-5487-4191-af86-2b7b7b3f2e1a	44a86e3c-9b8f-4331-801b-b88030479bce
b556fb9e-09c4-4b91-86dd-916afa75c911	3f3f7ecd-9c78-45e2-91d8-f5aea758f6ac
68b66fea-396d-4885-bda2-974f6ba5b133	5b6c3776-2028-4f8e-8e00-01e3575e9c0e
72bb35bf-3f54-401a-9d80-58d61df8901a	eda8a670-ba5a-4b85-b13f-8044f2e4fd57
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	c167eb61-1122-4d58-a2d5-1bd37807ea5e
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	990b52cb-5620-40d1-acf8-fe2345766c8c
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	86bfc8bb-898f-4bc2-bc94-77026cd1b715
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	d8599630-dca7-40e4-bbed-33161339c182
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	c6975a8d-7e0f-4586-ad62-708f1b19649d
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	b1148e7b-838e-411d-8ca1-cce658bdca72
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	971d448f-7575-4696-ad11-9de82f02d63d
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	ef4e04f8-34ef-4679-b162-6df6ae99be83
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	906a5c1f-a69b-4a3f-ba0a-dab5db2db8e8
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	f6e5f67c-6d32-4a8b-b116-acb38bfd3f32
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	276a93cc-0d73-4494-99e9-e68c07d7ec81
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	b2f86bac-b7a4-4e4e-86d8-661032b2819e
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	a6ccf2f7-3768-4c1a-b528-13d95aa65a05
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	654ed8a2-73b7-44fc-80d9-bef55d6c92ff
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	87de9812-e3ef-4903-830e-7572f63c63cd
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	ab142c47-546c-4522-ac40-3f903026b7ed
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	296cede5-2e72-4bd2-9e1a-8a93efecccd3
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	efa5841e-5c6e-46d7-9778-0f2c87b756ec
d8599630-dca7-40e4-bbed-33161339c182	87de9812-e3ef-4903-830e-7572f63c63cd
d8599630-dca7-40e4-bbed-33161339c182	efa5841e-5c6e-46d7-9778-0f2c87b756ec
c6975a8d-7e0f-4586-ad62-708f1b19649d	ab142c47-546c-4522-ac40-3f903026b7ed
cb922100-2875-4a8f-86ea-4534de6d8a97	eb456567-1eb4-460a-9497-383e20386102
cb922100-2875-4a8f-86ea-4534de6d8a97	265e76e9-12c4-4deb-bf74-a5983d2578b4
cb922100-2875-4a8f-86ea-4534de6d8a97	dbd38c4c-1454-44b0-a89b-ba25332dc4d3
cb922100-2875-4a8f-86ea-4534de6d8a97	b13f1a28-7a2d-4001-a53d-936340de1b5e
cb922100-2875-4a8f-86ea-4534de6d8a97	1abb2ba5-b5a8-4f8b-ac9f-a26c4d27344d
cb922100-2875-4a8f-86ea-4534de6d8a97	d84d5992-a169-4fdd-9b65-fc6d620cea7b
cb922100-2875-4a8f-86ea-4534de6d8a97	709b631c-722c-486b-bf95-e0f18c2866b8
cb922100-2875-4a8f-86ea-4534de6d8a97	86e92749-fae4-4600-bb60-46c363b0ad71
cb922100-2875-4a8f-86ea-4534de6d8a97	1fcb60d2-298b-4c5a-bda8-5588ae417f60
cb922100-2875-4a8f-86ea-4534de6d8a97	470a0f7a-549d-4601-80ea-470f1d6d9994
cb922100-2875-4a8f-86ea-4534de6d8a97	da3eb1e1-8705-46eb-a4f3-4511eb818d71
cb922100-2875-4a8f-86ea-4534de6d8a97	c3cc344b-77b3-40ae-b78a-5516ba2fca37
cb922100-2875-4a8f-86ea-4534de6d8a97	d261a97f-192c-47bb-8be2-b3db83f5b7e0
cb922100-2875-4a8f-86ea-4534de6d8a97	7e32416b-0977-4cf6-a4fc-d7d1d6242b4c
cb922100-2875-4a8f-86ea-4534de6d8a97	b3d9b79a-085f-4090-9e3f-8b29a87924ac
cb922100-2875-4a8f-86ea-4534de6d8a97	9de358c6-ea06-4f1b-8235-8cacb6bb8782
cb922100-2875-4a8f-86ea-4534de6d8a97	305265b5-8371-4abf-8e71-8207f9c43a8c
dbd38c4c-1454-44b0-a89b-ba25332dc4d3	305265b5-8371-4abf-8e71-8207f9c43a8c
dbd38c4c-1454-44b0-a89b-ba25332dc4d3	7e32416b-0977-4cf6-a4fc-d7d1d6242b4c
b13f1a28-7a2d-4001-a53d-936340de1b5e	b3d9b79a-085f-4090-9e3f-8b29a87924ac
cd62b709-9f11-4d60-b4af-270d69efc371	b2543bc1-6378-4bd2-9463-29db8428f994
20723ea1-e42a-4c9d-a151-cf17c041464c	d108c580-bf94-4155-b971-94b2a4508c4d
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	70649b4e-f277-48c0-865f-0b7dc62ba18f
cb922100-2875-4a8f-86ea-4534de6d8a97	15e3d0d9-b6b6-4d96-9dd1-7804118a84c7
\.


--
-- Data for Name: credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.credential (id, salt, type, user_id, created_date, user_label, secret_data, credential_data, priority) FROM stdin;
4660a7e0-b0a8-40b5-a6de-07e642c83807	\N	password	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911	1585788717824	\N	{"value":"rSXQR4y5XLIvWB+MCBv1NFYCPTBWLp8y5ErOf4hXgnzn8fljIjkTQj7HGAI89peYBkSBWca8lZYSOJHTMATVow==","salt":"Nyt78CypMTPBdJw4+Z7N9g=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
5a4100fe-da9b-4953-9b50-4840a6ff7552	\N	password	b2824e06-27cc-49a7-a767-9b5e37c9d651	1585846664794	\N	{"value":"EX6QGmFueWxomkB6PB5qxkO6GxUq75TBrs5CRd4L658iJUhswtBhSwLHLGwPtU0AT9lZYnvJ26PurjWs9I05mQ==","salt":"TNZ56Npw9qk6wpa137NSHA=="}	{"hashIterations":27500,"algorithm":"pbkdf2-sha256"}	10
\.


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
1.0.0.Final-KEYCLOAK-5461	sthorger@redhat.com	META-INF/jpa-changelog-1.0.0.Final.xml	2020-04-02 00:51:49.340204	1	EXECUTED	7:4e70412f24a3f382c82183742ec79317	createTable tableName=APPLICATION_DEFAULT_ROLES; createTable tableName=CLIENT; createTable tableName=CLIENT_SESSION; createTable tableName=CLIENT_SESSION_ROLE; createTable tableName=COMPOSITE_ROLE; createTable tableName=CREDENTIAL; createTable tab...		\N	3.5.4	\N	\N	5788708684
1.0.0.Final-KEYCLOAK-5461	sthorger@redhat.com	META-INF/db2-jpa-changelog-1.0.0.Final.xml	2020-04-02 00:51:49.354712	2	MARK_RAN	7:cb16724583e9675711801c6875114f28	createTable tableName=APPLICATION_DEFAULT_ROLES; createTable tableName=CLIENT; createTable tableName=CLIENT_SESSION; createTable tableName=CLIENT_SESSION_ROLE; createTable tableName=COMPOSITE_ROLE; createTable tableName=CREDENTIAL; createTable tab...		\N	3.5.4	\N	\N	5788708684
1.1.0.Beta1	sthorger@redhat.com	META-INF/jpa-changelog-1.1.0.Beta1.xml	2020-04-02 00:51:49.431681	3	EXECUTED	7:0310eb8ba07cec616460794d42ade0fa	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=CLIENT_ATTRIBUTES; createTable tableName=CLIENT_SESSION_NOTE; createTable tableName=APP_NODE_REGISTRATIONS; addColumn table...		\N	3.5.4	\N	\N	5788708684
1.1.0.Final	sthorger@redhat.com	META-INF/jpa-changelog-1.1.0.Final.xml	2020-04-02 00:51:49.440446	4	EXECUTED	7:5d25857e708c3233ef4439df1f93f012	renameColumn newColumnName=EVENT_TIME, oldColumnName=TIME, tableName=EVENT_ENTITY		\N	3.5.4	\N	\N	5788708684
1.2.0.Beta1	psilva@redhat.com	META-INF/jpa-changelog-1.2.0.Beta1.xml	2020-04-02 00:51:49.63909	5	EXECUTED	7:c7a54a1041d58eb3817a4a883b4d4e84	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=PROTOCOL_MAPPER; createTable tableName=PROTOCOL_MAPPER_CONFIG; createTable tableName=...		\N	3.5.4	\N	\N	5788708684
1.2.0.Beta1	psilva@redhat.com	META-INF/db2-jpa-changelog-1.2.0.Beta1.xml	2020-04-02 00:51:49.642684	6	MARK_RAN	7:2e01012df20974c1c2a605ef8afe25b7	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION; createTable tableName=PROTOCOL_MAPPER; createTable tableName=PROTOCOL_MAPPER_CONFIG; createTable tableName=...		\N	3.5.4	\N	\N	5788708684
1.2.0.RC1	bburke@redhat.com	META-INF/jpa-changelog-1.2.0.CR1.xml	2020-04-02 00:51:49.801916	7	EXECUTED	7:0f08df48468428e0f30ee59a8ec01a41	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=MIGRATION_MODEL; createTable tableName=IDENTITY_P...		\N	3.5.4	\N	\N	5788708684
1.2.0.RC1	bburke@redhat.com	META-INF/db2-jpa-changelog-1.2.0.CR1.xml	2020-04-02 00:51:49.808196	8	MARK_RAN	7:a77ea2ad226b345e7d689d366f185c8c	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=MIGRATION_MODEL; createTable tableName=IDENTITY_P...		\N	3.5.4	\N	\N	5788708684
1.2.0.Final	keycloak	META-INF/jpa-changelog-1.2.0.Final.xml	2020-04-02 00:51:49.817477	9	EXECUTED	7:a3377a2059aefbf3b90ebb4c4cc8e2ab	update tableName=CLIENT; update tableName=CLIENT; update tableName=CLIENT		\N	3.5.4	\N	\N	5788708684
1.3.0	bburke@redhat.com	META-INF/jpa-changelog-1.3.0.xml	2020-04-02 00:51:50.062496	10	EXECUTED	7:04c1dbedc2aa3e9756d1a1668e003451	delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete tableName=USER_SESSION; createTable tableName=ADMI...		\N	3.5.4	\N	\N	5788708684
1.4.0	bburke@redhat.com	META-INF/jpa-changelog-1.4.0.xml	2020-04-02 00:51:50.193938	11	EXECUTED	7:36ef39ed560ad07062d956db861042ba	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5788708684
1.4.0	bburke@redhat.com	META-INF/db2-jpa-changelog-1.4.0.xml	2020-04-02 00:51:50.214143	12	MARK_RAN	7:d909180b2530479a716d3f9c9eaea3d7	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5788708684
1.5.0	bburke@redhat.com	META-INF/jpa-changelog-1.5.0.xml	2020-04-02 00:51:50.23797	13	EXECUTED	7:cf12b04b79bea5152f165eb41f3955f6	delete tableName=CLIENT_SESSION_AUTH_STATUS; delete tableName=CLIENT_SESSION_ROLE; delete tableName=CLIENT_SESSION_PROT_MAPPER; delete tableName=CLIENT_SESSION_NOTE; delete tableName=CLIENT_SESSION; delete tableName=USER_SESSION_NOTE; delete table...		\N	3.5.4	\N	\N	5788708684
1.6.1_from15	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2020-04-02 00:51:50.294031	14	EXECUTED	7:7e32c8f05c755e8675764e7d5f514509	addColumn tableName=REALM; addColumn tableName=KEYCLOAK_ROLE; addColumn tableName=CLIENT; createTable tableName=OFFLINE_USER_SESSION; createTable tableName=OFFLINE_CLIENT_SESSION; addPrimaryKey constraintName=CONSTRAINT_OFFL_US_SES_PK2, tableName=...		\N	3.5.4	\N	\N	5788708684
1.6.1_from16-pre	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2020-04-02 00:51:50.301373	15	MARK_RAN	7:980ba23cc0ec39cab731ce903dd01291	delete tableName=OFFLINE_CLIENT_SESSION; delete tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	5788708684
1.6.1_from16	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2020-04-02 00:51:50.303181	16	MARK_RAN	7:2fa220758991285312eb84f3b4ff5336	dropPrimaryKey constraintName=CONSTRAINT_OFFLINE_US_SES_PK, tableName=OFFLINE_USER_SESSION; dropPrimaryKey constraintName=CONSTRAINT_OFFLINE_CL_SES_PK, tableName=OFFLINE_CLIENT_SESSION; addColumn tableName=OFFLINE_USER_SESSION; update tableName=OF...		\N	3.5.4	\N	\N	5788708684
1.6.1	mposolda@redhat.com	META-INF/jpa-changelog-1.6.1.xml	2020-04-02 00:51:50.304595	17	EXECUTED	7:d41d8cd98f00b204e9800998ecf8427e	empty		\N	3.5.4	\N	\N	5788708684
1.7.0	bburke@redhat.com	META-INF/jpa-changelog-1.7.0.xml	2020-04-02 00:51:50.38679	18	EXECUTED	7:91ace540896df890cc00a0490ee52bbc	createTable tableName=KEYCLOAK_GROUP; createTable tableName=GROUP_ROLE_MAPPING; createTable tableName=GROUP_ATTRIBUTE; createTable tableName=USER_GROUP_MEMBERSHIP; createTable tableName=REALM_DEFAULT_GROUPS; addColumn tableName=IDENTITY_PROVIDER; ...		\N	3.5.4	\N	\N	5788708684
1.8.0	mposolda@redhat.com	META-INF/jpa-changelog-1.8.0.xml	2020-04-02 00:51:50.466471	19	EXECUTED	7:c31d1646dfa2618a9335c00e07f89f24	addColumn tableName=IDENTITY_PROVIDER; createTable tableName=CLIENT_TEMPLATE; createTable tableName=CLIENT_TEMPLATE_ATTRIBUTES; createTable tableName=TEMPLATE_SCOPE_MAPPING; dropNotNullConstraint columnName=CLIENT_ID, tableName=PROTOCOL_MAPPER; ad...		\N	3.5.4	\N	\N	5788708684
1.8.0-2	keycloak	META-INF/jpa-changelog-1.8.0.xml	2020-04-02 00:51:50.476761	20	EXECUTED	7:df8bc21027a4f7cbbb01f6344e89ce07	dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; update tableName=CREDENTIAL		\N	3.5.4	\N	\N	5788708684
authz-3.4.0.CR1-resource-server-pk-change-part1	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2020-04-02 00:51:51.78702	45	EXECUTED	7:6a48ce645a3525488a90fbf76adf3bb3	addColumn tableName=RESOURCE_SERVER_POLICY; addColumn tableName=RESOURCE_SERVER_RESOURCE; addColumn tableName=RESOURCE_SERVER_SCOPE		\N	3.5.4	\N	\N	5788708684
1.8.0	mposolda@redhat.com	META-INF/db2-jpa-changelog-1.8.0.xml	2020-04-02 00:51:50.484464	21	MARK_RAN	7:f987971fe6b37d963bc95fee2b27f8df	addColumn tableName=IDENTITY_PROVIDER; createTable tableName=CLIENT_TEMPLATE; createTable tableName=CLIENT_TEMPLATE_ATTRIBUTES; createTable tableName=TEMPLATE_SCOPE_MAPPING; dropNotNullConstraint columnName=CLIENT_ID, tableName=PROTOCOL_MAPPER; ad...		\N	3.5.4	\N	\N	5788708684
1.8.0-2	keycloak	META-INF/db2-jpa-changelog-1.8.0.xml	2020-04-02 00:51:50.492606	22	MARK_RAN	7:df8bc21027a4f7cbbb01f6344e89ce07	dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; update tableName=CREDENTIAL		\N	3.5.4	\N	\N	5788708684
1.9.0	mposolda@redhat.com	META-INF/jpa-changelog-1.9.0.xml	2020-04-02 00:51:50.532308	23	EXECUTED	7:ed2dc7f799d19ac452cbcda56c929e47	update tableName=REALM; update tableName=REALM; update tableName=REALM; update tableName=REALM; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=REALM; update tableName=REALM; customChange; dr...		\N	3.5.4	\N	\N	5788708684
1.9.1	keycloak	META-INF/jpa-changelog-1.9.1.xml	2020-04-02 00:51:50.544464	24	EXECUTED	7:80b5db88a5dda36ece5f235be8757615	modifyDataType columnName=PRIVATE_KEY, tableName=REALM; modifyDataType columnName=PUBLIC_KEY, tableName=REALM; modifyDataType columnName=CERTIFICATE, tableName=REALM		\N	3.5.4	\N	\N	5788708684
1.9.1	keycloak	META-INF/db2-jpa-changelog-1.9.1.xml	2020-04-02 00:51:50.547215	25	MARK_RAN	7:1437310ed1305a9b93f8848f301726ce	modifyDataType columnName=PRIVATE_KEY, tableName=REALM; modifyDataType columnName=CERTIFICATE, tableName=REALM		\N	3.5.4	\N	\N	5788708684
1.9.2	keycloak	META-INF/jpa-changelog-1.9.2.xml	2020-04-02 00:51:50.67525	26	EXECUTED	7:b82ffb34850fa0836be16deefc6a87c4	createIndex indexName=IDX_USER_EMAIL, tableName=USER_ENTITY; createIndex indexName=IDX_USER_ROLE_MAPPING, tableName=USER_ROLE_MAPPING; createIndex indexName=IDX_USER_GROUP_MAPPING, tableName=USER_GROUP_MEMBERSHIP; createIndex indexName=IDX_USER_CO...		\N	3.5.4	\N	\N	5788708684
authz-2.0.0	psilva@redhat.com	META-INF/jpa-changelog-authz-2.0.0.xml	2020-04-02 00:51:50.895556	27	EXECUTED	7:9cc98082921330d8d9266decdd4bd658	createTable tableName=RESOURCE_SERVER; addPrimaryKey constraintName=CONSTRAINT_FARS, tableName=RESOURCE_SERVER; addUniqueConstraint constraintName=UK_AU8TT6T700S9V50BU18WS5HA6, tableName=RESOURCE_SERVER; createTable tableName=RESOURCE_SERVER_RESOU...		\N	3.5.4	\N	\N	5788708684
authz-2.5.1	psilva@redhat.com	META-INF/jpa-changelog-authz-2.5.1.xml	2020-04-02 00:51:50.904327	28	EXECUTED	7:03d64aeed9cb52b969bd30a7ac0db57e	update tableName=RESOURCE_SERVER_POLICY		\N	3.5.4	\N	\N	5788708684
2.1.0-KEYCLOAK-5461	bburke@redhat.com	META-INF/jpa-changelog-2.1.0.xml	2020-04-02 00:51:51.097918	29	EXECUTED	7:f1f9fd8710399d725b780f463c6b21cd	createTable tableName=BROKER_LINK; createTable tableName=FED_USER_ATTRIBUTE; createTable tableName=FED_USER_CONSENT; createTable tableName=FED_USER_CONSENT_ROLE; createTable tableName=FED_USER_CONSENT_PROT_MAPPER; createTable tableName=FED_USER_CR...		\N	3.5.4	\N	\N	5788708684
2.2.0	bburke@redhat.com	META-INF/jpa-changelog-2.2.0.xml	2020-04-02 00:51:51.124855	30	EXECUTED	7:53188c3eb1107546e6f765835705b6c1	addColumn tableName=ADMIN_EVENT_ENTITY; createTable tableName=CREDENTIAL_ATTRIBUTE; createTable tableName=FED_CREDENTIAL_ATTRIBUTE; modifyDataType columnName=VALUE, tableName=CREDENTIAL; addForeignKeyConstraint baseTableName=FED_CREDENTIAL_ATTRIBU...		\N	3.5.4	\N	\N	5788708684
2.3.0	bburke@redhat.com	META-INF/jpa-changelog-2.3.0.xml	2020-04-02 00:51:51.157436	31	EXECUTED	7:d6e6f3bc57a0c5586737d1351725d4d4	createTable tableName=FEDERATED_USER; addPrimaryKey constraintName=CONSTR_FEDERATED_USER, tableName=FEDERATED_USER; dropDefaultValue columnName=TOTP, tableName=USER_ENTITY; dropColumn columnName=TOTP, tableName=USER_ENTITY; addColumn tableName=IDE...		\N	3.5.4	\N	\N	5788708684
2.4.0	bburke@redhat.com	META-INF/jpa-changelog-2.4.0.xml	2020-04-02 00:51:51.167337	32	EXECUTED	7:454d604fbd755d9df3fd9c6329043aa5	customChange		\N	3.5.4	\N	\N	5788708684
2.5.0	bburke@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2020-04-02 00:51:51.182551	33	EXECUTED	7:57e98a3077e29caf562f7dbf80c72600	customChange; modifyDataType columnName=USER_ID, tableName=OFFLINE_USER_SESSION		\N	3.5.4	\N	\N	5788708684
2.5.0-unicode-oracle	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2020-04-02 00:51:51.184566	34	MARK_RAN	7:e4c7e8f2256210aee71ddc42f538b57a	modifyDataType columnName=DESCRIPTION, tableName=AUTHENTICATION_FLOW; modifyDataType columnName=DESCRIPTION, tableName=CLIENT_TEMPLATE; modifyDataType columnName=DESCRIPTION, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=DESCRIPTION,...		\N	3.5.4	\N	\N	5788708684
2.5.0-unicode-other-dbs	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2020-04-02 00:51:51.241462	35	EXECUTED	7:09a43c97e49bc626460480aa1379b522	modifyDataType columnName=DESCRIPTION, tableName=AUTHENTICATION_FLOW; modifyDataType columnName=DESCRIPTION, tableName=CLIENT_TEMPLATE; modifyDataType columnName=DESCRIPTION, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=DESCRIPTION,...		\N	3.5.4	\N	\N	5788708684
2.5.0-duplicate-email-support	slawomir@dabek.name	META-INF/jpa-changelog-2.5.0.xml	2020-04-02 00:51:51.246296	36	EXECUTED	7:26bfc7c74fefa9126f2ce702fb775553	addColumn tableName=REALM		\N	3.5.4	\N	\N	5788708684
2.5.0-unique-group-names	hmlnarik@redhat.com	META-INF/jpa-changelog-2.5.0.xml	2020-04-02 00:51:51.263521	37	EXECUTED	7:a161e2ae671a9020fff61e996a207377	addUniqueConstraint constraintName=SIBLING_NAMES, tableName=KEYCLOAK_GROUP		\N	3.5.4	\N	\N	5788708684
2.5.1	bburke@redhat.com	META-INF/jpa-changelog-2.5.1.xml	2020-04-02 00:51:51.266549	38	EXECUTED	7:37fc1781855ac5388c494f1442b3f717	addColumn tableName=FED_USER_CONSENT		\N	3.5.4	\N	\N	5788708684
3.0.0	bburke@redhat.com	META-INF/jpa-changelog-3.0.0.xml	2020-04-02 00:51:51.269583	39	EXECUTED	7:13a27db0dae6049541136adad7261d27	addColumn tableName=IDENTITY_PROVIDER		\N	3.5.4	\N	\N	5788708684
3.2.0-fix	keycloak	META-INF/jpa-changelog-3.2.0.xml	2020-04-02 00:51:51.271394	40	MARK_RAN	7:550300617e3b59e8af3a6294df8248a3	addNotNullConstraint columnName=REALM_ID, tableName=CLIENT_INITIAL_ACCESS		\N	3.5.4	\N	\N	5788708684
3.2.0-fix-with-keycloak-5416	keycloak	META-INF/jpa-changelog-3.2.0.xml	2020-04-02 00:51:51.273251	41	MARK_RAN	7:e3a9482b8931481dc2772a5c07c44f17	dropIndex indexName=IDX_CLIENT_INIT_ACC_REALM, tableName=CLIENT_INITIAL_ACCESS; addNotNullConstraint columnName=REALM_ID, tableName=CLIENT_INITIAL_ACCESS; createIndex indexName=IDX_CLIENT_INIT_ACC_REALM, tableName=CLIENT_INITIAL_ACCESS		\N	3.5.4	\N	\N	5788708684
3.2.0-fix-offline-sessions	hmlnarik	META-INF/jpa-changelog-3.2.0.xml	2020-04-02 00:51:51.284756	42	EXECUTED	7:72b07d85a2677cb257edb02b408f332d	customChange		\N	3.5.4	\N	\N	5788708684
3.2.0-fixed	keycloak	META-INF/jpa-changelog-3.2.0.xml	2020-04-02 00:51:51.757717	43	EXECUTED	7:a72a7858967bd414835d19e04d880312	addColumn tableName=REALM; dropPrimaryKey constraintName=CONSTRAINT_OFFL_CL_SES_PK2, tableName=OFFLINE_CLIENT_SESSION; dropColumn columnName=CLIENT_SESSION_ID, tableName=OFFLINE_CLIENT_SESSION; addPrimaryKey constraintName=CONSTRAINT_OFFL_CL_SES_P...		\N	3.5.4	\N	\N	5788708684
3.3.0	keycloak	META-INF/jpa-changelog-3.3.0.xml	2020-04-02 00:51:51.775188	44	EXECUTED	7:94edff7cf9ce179e7e85f0cd78a3cf2c	addColumn tableName=USER_ENTITY		\N	3.5.4	\N	\N	5788708684
authz-3.4.0.CR1-resource-server-pk-change-part2-KEYCLOAK-6095	hmlnarik@redhat.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2020-04-02 00:51:51.793722	46	EXECUTED	7:e64b5dcea7db06077c6e57d3b9e5ca14	customChange		\N	3.5.4	\N	\N	5788708684
authz-3.4.0.CR1-resource-server-pk-change-part3-fixed	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2020-04-02 00:51:51.795869	47	MARK_RAN	7:fd8cf02498f8b1e72496a20afc75178c	dropIndex indexName=IDX_RES_SERV_POL_RES_SERV, tableName=RESOURCE_SERVER_POLICY; dropIndex indexName=IDX_RES_SRV_RES_RES_SRV, tableName=RESOURCE_SERVER_RESOURCE; dropIndex indexName=IDX_RES_SRV_SCOPE_RES_SRV, tableName=RESOURCE_SERVER_SCOPE		\N	3.5.4	\N	\N	5788708684
authz-3.4.0.CR1-resource-server-pk-change-part3-fixed-nodropindex	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2020-04-02 00:51:51.906969	48	EXECUTED	7:542794f25aa2b1fbabb7e577d6646319	addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, tableName=RESOURCE_SERVER_POLICY; addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, tableName=RESOURCE_SERVER_RESOURCE; addNotNullConstraint columnName=RESOURCE_SERVER_CLIENT_ID, ...		\N	3.5.4	\N	\N	5788708684
authn-3.4.0.CR1-refresh-token-max-reuse	glavoie@gmail.com	META-INF/jpa-changelog-authz-3.4.0.CR1.xml	2020-04-02 00:51:51.922453	49	EXECUTED	7:edad604c882df12f74941dac3cc6d650	addColumn tableName=REALM		\N	3.5.4	\N	\N	5788708684
3.4.0	keycloak	META-INF/jpa-changelog-3.4.0.xml	2020-04-02 00:51:52.066324	50	EXECUTED	7:0f88b78b7b46480eb92690cbf5e44900	addPrimaryKey constraintName=CONSTRAINT_REALM_DEFAULT_ROLES, tableName=REALM_DEFAULT_ROLES; addPrimaryKey constraintName=CONSTRAINT_COMPOSITE_ROLE, tableName=COMPOSITE_ROLE; addPrimaryKey constraintName=CONSTR_REALM_DEFAULT_GROUPS, tableName=REALM...		\N	3.5.4	\N	\N	5788708684
3.4.0-KEYCLOAK-5230	hmlnarik@redhat.com	META-INF/jpa-changelog-3.4.0.xml	2020-04-02 00:51:52.195913	51	EXECUTED	7:d560e43982611d936457c327f872dd59	createIndex indexName=IDX_FU_ATTRIBUTE, tableName=FED_USER_ATTRIBUTE; createIndex indexName=IDX_FU_CONSENT, tableName=FED_USER_CONSENT; createIndex indexName=IDX_FU_CONSENT_RU, tableName=FED_USER_CONSENT; createIndex indexName=IDX_FU_CREDENTIAL, t...		\N	3.5.4	\N	\N	5788708684
3.4.1	psilva@redhat.com	META-INF/jpa-changelog-3.4.1.xml	2020-04-02 00:51:52.21063	52	EXECUTED	7:c155566c42b4d14ef07059ec3b3bbd8e	modifyDataType columnName=VALUE, tableName=CLIENT_ATTRIBUTES		\N	3.5.4	\N	\N	5788708684
3.4.2	keycloak	META-INF/jpa-changelog-3.4.2.xml	2020-04-02 00:51:52.219572	53	EXECUTED	7:b40376581f12d70f3c89ba8ddf5b7dea	update tableName=REALM		\N	3.5.4	\N	\N	5788708684
3.4.2-KEYCLOAK-5172	mkanis@redhat.com	META-INF/jpa-changelog-3.4.2.xml	2020-04-02 00:51:52.230106	54	EXECUTED	7:a1132cc395f7b95b3646146c2e38f168	update tableName=CLIENT		\N	3.5.4	\N	\N	5788708684
4.0.0-KEYCLOAK-6335	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2020-04-02 00:51:52.243136	55	EXECUTED	7:d8dc5d89c789105cfa7ca0e82cba60af	createTable tableName=CLIENT_AUTH_FLOW_BINDINGS; addPrimaryKey constraintName=C_CLI_FLOW_BIND, tableName=CLIENT_AUTH_FLOW_BINDINGS		\N	3.5.4	\N	\N	5788708684
4.0.0-CLEANUP-UNUSED-TABLE	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2020-04-02 00:51:52.265253	56	EXECUTED	7:7822e0165097182e8f653c35517656a3	dropTable tableName=CLIENT_IDENTITY_PROV_MAPPING		\N	3.5.4	\N	\N	5788708684
4.0.0-KEYCLOAK-6228	bburke@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2020-04-02 00:51:52.324067	57	EXECUTED	7:c6538c29b9c9a08f9e9ea2de5c2b6375	dropUniqueConstraint constraintName=UK_JKUWUVD56ONTGSUHOGM8UEWRT, tableName=USER_CONSENT; dropNotNullConstraint columnName=CLIENT_ID, tableName=USER_CONSENT; addColumn tableName=USER_CONSENT; addUniqueConstraint constraintName=UK_JKUWUVD56ONTGSUHO...		\N	3.5.4	\N	\N	5788708684
4.0.0-KEYCLOAK-5579-fixed	mposolda@redhat.com	META-INF/jpa-changelog-4.0.0.xml	2020-04-02 00:51:52.571319	58	EXECUTED	7:6d4893e36de22369cf73bcb051ded875	dropForeignKeyConstraint baseTableName=CLIENT_TEMPLATE_ATTRIBUTES, constraintName=FK_CL_TEMPL_ATTR_TEMPL; renameTable newTableName=CLIENT_SCOPE_ATTRIBUTES, oldTableName=CLIENT_TEMPLATE_ATTRIBUTES; renameColumn newColumnName=SCOPE_ID, oldColumnName...		\N	3.5.4	\N	\N	5788708684
authz-4.0.0.CR1	psilva@redhat.com	META-INF/jpa-changelog-authz-4.0.0.CR1.xml	2020-04-02 00:51:52.634937	59	EXECUTED	7:57960fc0b0f0dd0563ea6f8b2e4a1707	createTable tableName=RESOURCE_SERVER_PERM_TICKET; addPrimaryKey constraintName=CONSTRAINT_FAPMT, tableName=RESOURCE_SERVER_PERM_TICKET; addForeignKeyConstraint baseTableName=RESOURCE_SERVER_PERM_TICKET, constraintName=FK_FRSRHO213XCX4WNKOG82SSPMT...		\N	3.5.4	\N	\N	5788708684
authz-4.0.0.Beta3	psilva@redhat.com	META-INF/jpa-changelog-authz-4.0.0.Beta3.xml	2020-04-02 00:51:52.657351	60	EXECUTED	7:2b4b8bff39944c7097977cc18dbceb3b	addColumn tableName=RESOURCE_SERVER_POLICY; addColumn tableName=RESOURCE_SERVER_PERM_TICKET; addForeignKeyConstraint baseTableName=RESOURCE_SERVER_PERM_TICKET, constraintName=FK_FRSRPO2128CX4WNKOG82SSRFY, referencedTableName=RESOURCE_SERVER_POLICY		\N	3.5.4	\N	\N	5788708684
authz-4.2.0.Final	mhajas@redhat.com	META-INF/jpa-changelog-authz-4.2.0.Final.xml	2020-04-02 00:51:52.670784	61	EXECUTED	7:2aa42a964c59cd5b8ca9822340ba33a8	createTable tableName=RESOURCE_URIS; addForeignKeyConstraint baseTableName=RESOURCE_URIS, constraintName=FK_RESOURCE_SERVER_URIS, referencedTableName=RESOURCE_SERVER_RESOURCE; customChange; dropColumn columnName=URI, tableName=RESOURCE_SERVER_RESO...		\N	3.5.4	\N	\N	5788708684
authz-4.2.0.Final-KEYCLOAK-9944	hmlnarik@redhat.com	META-INF/jpa-changelog-authz-4.2.0.Final.xml	2020-04-02 00:51:52.684068	62	EXECUTED	7:9ac9e58545479929ba23f4a3087a0346	addPrimaryKey constraintName=CONSTRAINT_RESOUR_URIS_PK, tableName=RESOURCE_URIS		\N	3.5.4	\N	\N	5788708684
4.2.0-KEYCLOAK-6313	wadahiro@gmail.com	META-INF/jpa-changelog-4.2.0.xml	2020-04-02 00:51:52.693977	63	EXECUTED	7:14d407c35bc4fe1976867756bcea0c36	addColumn tableName=REQUIRED_ACTION_PROVIDER		\N	3.5.4	\N	\N	5788708684
4.3.0-KEYCLOAK-7984	wadahiro@gmail.com	META-INF/jpa-changelog-4.3.0.xml	2020-04-02 00:51:52.702232	64	EXECUTED	7:241a8030c748c8548e346adee548fa93	update tableName=REQUIRED_ACTION_PROVIDER		\N	3.5.4	\N	\N	5788708684
4.6.0-KEYCLOAK-7950	psilva@redhat.com	META-INF/jpa-changelog-4.6.0.xml	2020-04-02 00:51:52.710225	65	EXECUTED	7:7d3182f65a34fcc61e8d23def037dc3f	update tableName=RESOURCE_SERVER_RESOURCE		\N	3.5.4	\N	\N	5788708684
4.6.0-KEYCLOAK-8377	keycloak	META-INF/jpa-changelog-4.6.0.xml	2020-04-02 00:51:52.75102	66	EXECUTED	7:b30039e00a0b9715d430d1b0636728fa	createTable tableName=ROLE_ATTRIBUTE; addPrimaryKey constraintName=CONSTRAINT_ROLE_ATTRIBUTE_PK, tableName=ROLE_ATTRIBUTE; addForeignKeyConstraint baseTableName=ROLE_ATTRIBUTE, constraintName=FK_ROLE_ATTRIBUTE_ID, referencedTableName=KEYCLOAK_ROLE...		\N	3.5.4	\N	\N	5788708684
4.6.0-KEYCLOAK-8555	gideonray@gmail.com	META-INF/jpa-changelog-4.6.0.xml	2020-04-02 00:51:52.769796	67	EXECUTED	7:3797315ca61d531780f8e6f82f258159	createIndex indexName=IDX_COMPONENT_PROVIDER_TYPE, tableName=COMPONENT		\N	3.5.4	\N	\N	5788708684
4.7.0-KEYCLOAK-1267	sguilhen@redhat.com	META-INF/jpa-changelog-4.7.0.xml	2020-04-02 00:51:52.776024	68	EXECUTED	7:c7aa4c8d9573500c2d347c1941ff0301	addColumn tableName=REALM		\N	3.5.4	\N	\N	5788708684
4.7.0-KEYCLOAK-7275	keycloak	META-INF/jpa-changelog-4.7.0.xml	2020-04-02 00:51:52.802206	69	EXECUTED	7:b207faee394fc074a442ecd42185a5dd	renameColumn newColumnName=CREATED_ON, oldColumnName=LAST_SESSION_REFRESH, tableName=OFFLINE_USER_SESSION; addNotNullConstraint columnName=CREATED_ON, tableName=OFFLINE_USER_SESSION; addColumn tableName=OFFLINE_USER_SESSION; customChange; createIn...		\N	3.5.4	\N	\N	5788708684
4.8.0-KEYCLOAK-8835	sguilhen@redhat.com	META-INF/jpa-changelog-4.8.0.xml	2020-04-02 00:51:52.822649	70	EXECUTED	7:ab9a9762faaba4ddfa35514b212c4922	addNotNullConstraint columnName=SSO_MAX_LIFESPAN_REMEMBER_ME, tableName=REALM; addNotNullConstraint columnName=SSO_IDLE_TIMEOUT_REMEMBER_ME, tableName=REALM		\N	3.5.4	\N	\N	5788708684
authz-7.0.0-KEYCLOAK-10443	psilva@redhat.com	META-INF/jpa-changelog-authz-7.0.0.xml	2020-04-02 00:51:52.828275	71	EXECUTED	7:b9710f74515a6ccb51b72dc0d19df8c4	addColumn tableName=RESOURCE_SERVER		\N	3.5.4	\N	\N	5788708684
8.0.0-adding-credential-columns	keycloak	META-INF/jpa-changelog-8.0.0.xml	2020-04-02 00:51:52.837069	72	EXECUTED	7:ec9707ae4d4f0b7452fee20128083879	addColumn tableName=CREDENTIAL; addColumn tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	5788708684
8.0.0-updating-credential-data-not-oracle	keycloak	META-INF/jpa-changelog-8.0.0.xml	2020-04-02 00:51:52.846575	73	EXECUTED	7:03b3f4b264c3c68ba082250a80b74216	update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	5788708684
8.0.0-updating-credential-data-oracle	keycloak	META-INF/jpa-changelog-8.0.0.xml	2020-04-02 00:51:52.860717	74	MARK_RAN	7:64c5728f5ca1f5aa4392217701c4fe23	update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL; update tableName=FED_USER_CREDENTIAL		\N	3.5.4	\N	\N	5788708684
8.0.0-credential-cleanup	keycloak	META-INF/jpa-changelog-8.0.0.xml	2020-04-02 00:51:52.887362	75	EXECUTED	7:41f3566ac5177459e1ed3ce8f0ad35d2	dropDefaultValue columnName=COUNTER, tableName=CREDENTIAL; dropDefaultValue columnName=DIGITS, tableName=CREDENTIAL; dropDefaultValue columnName=PERIOD, tableName=CREDENTIAL; dropDefaultValue columnName=ALGORITHM, tableName=CREDENTIAL; dropColumn ...		\N	3.5.4	\N	\N	5788708684
8.0.0-resource-tag-support	keycloak	META-INF/jpa-changelog-8.0.0.xml	2020-04-02 00:51:52.90554	76	EXECUTED	7:a73379915c23bfad3e8f5c6d5c0aa4bd	addColumn tableName=MIGRATION_MODEL; createIndex indexName=IDX_UPDATE_TIME, tableName=MIGRATION_MODEL		\N	3.5.4	\N	\N	5788708684
9.0.0-always-display-client	keycloak	META-INF/jpa-changelog-9.0.0.xml	2020-04-02 00:51:52.920246	77	EXECUTED	7:39e0073779aba192646291aa2332493d	addColumn tableName=CLIENT		\N	3.5.4	\N	\N	5788708684
9.0.0-drop-constraints-for-column-increase	keycloak	META-INF/jpa-changelog-9.0.0.xml	2020-04-02 00:51:52.928355	78	MARK_RAN	7:81f87368f00450799b4bf42ea0b3ec34	dropUniqueConstraint constraintName=UK_FRSR6T700S9V50BU18WS5PMT, tableName=RESOURCE_SERVER_PERM_TICKET; dropUniqueConstraint constraintName=UK_FRSR6T700S9V50BU18WS5HA6, tableName=RESOURCE_SERVER_RESOURCE; dropPrimaryKey constraintName=CONSTRAINT_O...		\N	3.5.4	\N	\N	5788708684
9.0.0-increase-column-size-federated-fk	keycloak	META-INF/jpa-changelog-9.0.0.xml	2020-04-02 00:51:52.978143	79	EXECUTED	7:20b37422abb9fb6571c618148f013a15	modifyDataType columnName=CLIENT_ID, tableName=FED_USER_CONSENT; modifyDataType columnName=CLIENT_REALM_CONSTRAINT, tableName=KEYCLOAK_ROLE; modifyDataType columnName=OWNER, tableName=RESOURCE_SERVER_POLICY; modifyDataType columnName=CLIENT_ID, ta...		\N	3.5.4	\N	\N	5788708684
9.0.0-recreate-constraints-after-column-increase	keycloak	META-INF/jpa-changelog-9.0.0.xml	2020-04-02 00:51:52.979858	80	MARK_RAN	7:1970bb6cfb5ee800736b95ad3fb3c78a	addNotNullConstraint columnName=CLIENT_ID, tableName=OFFLINE_CLIENT_SESSION; addNotNullConstraint columnName=OWNER, tableName=RESOURCE_SERVER_PERM_TICKET; addNotNullConstraint columnName=REQUESTER, tableName=RESOURCE_SERVER_PERM_TICKET; addNotNull...		\N	3.5.4	\N	\N	5788708684
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
1000	f	\N	\N
1001	f	\N	\N
\.


--
-- Data for Name: default_client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.default_client_scope (realm_id, scope_id, default_scope) FROM stdin;
master	f20b7e12-cbf7-4cf2-92e0-ab8245256b83	f
master	952c33c7-6e1a-4166-a2b6-781c4d97c9ad	t
master	6fb85823-f6c8-416a-b77d-24f21f73eef3	t
master	a1156a4d-3edf-4e46-8802-dc8f7d071c94	t
master	7215e639-b32b-4edc-89fa-109375845473	f
master	af1583de-b675-4dfb-bea4-a3c74d82eaad	f
master	1a5c13e3-16a7-46ca-9833-64dbb4541034	t
master	1e4543a6-ac19-4298-9722-f555758997f5	t
master	396a8291-b64d-4f42-8940-14c424b5598c	f
Citygroves	3c8e4d35-bffe-478d-8cb1-36cc46c89663	f
Citygroves	b3d82398-6878-4915-a7f1-99ff0ed9a1c0	t
Citygroves	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e	t
Citygroves	bcb82f70-fd63-4933-829f-183158674f81	t
Citygroves	c9fbc7ca-d340-460d-abee-9c619f8de40c	f
Citygroves	a72c9669-7fec-43a0-b467-8f2afdc9640d	f
Citygroves	0f29d097-c464-4c81-a65d-304a401d1c96	t
Citygroves	bb86f232-3c7e-4409-9de7-c0641a261793	t
Citygroves	9b593dbb-eadb-47ec-badb-bcce9ab0c11f	f
\.


--
-- Data for Name: event_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.event_entity (id, client_id, details_json, error, ip_address, realm_id, session_id, event_time, type, user_id) FROM stdin;
\.


--
-- Data for Name: fed_user_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_attribute (id, name, user_id, realm_id, storage_provider_id, value) FROM stdin;
\.


--
-- Data for Name: fed_user_consent; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_consent (id, client_id, user_id, realm_id, storage_provider_id, created_date, last_updated_date, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: fed_user_consent_cl_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_consent_cl_scope (user_consent_id, scope_id) FROM stdin;
\.


--
-- Data for Name: fed_user_credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_credential (id, salt, type, created_date, user_id, realm_id, storage_provider_id, user_label, secret_data, credential_data, priority) FROM stdin;
\.


--
-- Data for Name: fed_user_group_membership; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_group_membership (group_id, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: fed_user_required_action; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_required_action (required_action, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: fed_user_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.fed_user_role_mapping (role_id, user_id, realm_id, storage_provider_id) FROM stdin;
\.


--
-- Data for Name: federated_identity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.federated_identity (identity_provider, realm_id, federated_user_id, federated_username, token, user_id) FROM stdin;
\.


--
-- Data for Name: federated_user; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.federated_user (id, storage_provider_id, realm_id) FROM stdin;
\.


--
-- Data for Name: group_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.group_attribute (id, name, value, group_id) FROM stdin;
\.


--
-- Data for Name: group_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.group_role_mapping (role_id, group_id) FROM stdin;
\.


--
-- Data for Name: identity_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider (internal_id, enabled, provider_alias, provider_id, store_token, authenticate_by_default, realm_id, add_token_role, trust_email, first_broker_login_flow_id, post_broker_login_flow_id, provider_display_name, link_only) FROM stdin;
\.


--
-- Data for Name: identity_provider_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider_config (identity_provider_id, value, name) FROM stdin;
\.


--
-- Data for Name: identity_provider_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.identity_provider_mapper (id, name, idp_alias, idp_mapper_name, realm_id) FROM stdin;
\.


--
-- Data for Name: idp_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.idp_mapper_config (idp_mapper_id, value, name) FROM stdin;
\.


--
-- Data for Name: keycloak_group; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.keycloak_group (id, name, parent_group, realm_id) FROM stdin;
\.


--
-- Data for Name: keycloak_role; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.keycloak_role (id, client_realm_constraint, client_role, description, name, realm_id, client, realm) FROM stdin;
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	master	f	${role_admin}	admin	master	\N	master
23a20ea9-7cd4-4dd9-bd24-38011be8b322	master	f	${role_create-realm}	create-realm	master	\N	master
76a96647-e367-42cf-8c70-5fc5ad5e1da0	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_create-client}	create-client	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
065ac91d-c450-4dcb-ac2f-0edadfd26a08	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-realm}	view-realm	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
4e857f49-5487-4191-af86-2b7b7b3f2e1a	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-users}	view-users	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
b556fb9e-09c4-4b91-86dd-916afa75c911	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-clients}	view-clients	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
f78ac3ef-5e25-4925-8fc8-69c1135a8543	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-events}	view-events	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
e169fa79-ed79-4090-9535-c7e8099ce26b	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-identity-providers}	view-identity-providers	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
01f89448-3b46-4a8a-b8b2-1cd291fb185a	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_view-authorization}	view-authorization	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
02bef763-579f-4fc2-826f-f62198dba9ce	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-realm}	manage-realm	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
bd868368-8c11-4196-b88a-20c17dcbd4c5	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-users}	manage-users	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
1a051660-cf53-414e-bcee-a4bb4b792466	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-clients}	manage-clients	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
90a63da7-d46d-4732-a5e6-5f7f4ba53061	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-events}	manage-events	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
c80801d4-b6d0-445b-a8d6-2fb498792963	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-identity-providers}	manage-identity-providers	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
ba9db82c-8285-48bd-950e-99865b6874eb	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_manage-authorization}	manage-authorization	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
27abfef1-64d5-44ea-b1d5-63154e3a9d16	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_query-users}	query-users	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
3f3f7ecd-9c78-45e2-91d8-f5aea758f6ac	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_query-clients}	query-clients	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
b50cfdd3-41b5-43cd-b008-1d6b07e4b8ba	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_query-realms}	query-realms	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
44a86e3c-9b8f-4331-801b-b88030479bce	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_query-groups}	query-groups	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
0e2a4fc9-bc35-4a6f-ac4a-d372f691f5fd	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_view-profile}	view-profile	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
68b66fea-396d-4885-bda2-974f6ba5b133	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_manage-account}	manage-account	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
5b6c3776-2028-4f8e-8e00-01e3575e9c0e	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_manage-account-links}	manage-account-links	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
e850c9a8-1dbd-4d79-b92d-ee9ac7310fac	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_view-applications}	view-applications	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
eda8a670-ba5a-4b85-b13f-8044f2e4fd57	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_view-consent}	view-consent	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
72bb35bf-3f54-401a-9d80-58d61df8901a	ce09c09e-54bb-4a0a-8b6d-651c069c0361	t	${role_manage-consent}	manage-consent	master	ce09c09e-54bb-4a0a-8b6d-651c069c0361	\N
7c24b5df-546a-400e-8016-06fef6a55816	e66e1263-40c9-41af-9b09-8a1699959949	t	${role_read-token}	read-token	master	e66e1263-40c9-41af-9b09-8a1699959949	\N
c167eb61-1122-4d58-a2d5-1bd37807ea5e	b1f65320-f3da-48ee-9db1-d5b305f1c855	t	${role_impersonation}	impersonation	master	b1f65320-f3da-48ee-9db1-d5b305f1c855	\N
f6c96cdc-4f19-4bde-bea5-6edef4d84f7a	master	f	${role_offline-access}	offline_access	master	\N	master
7c2827b5-9734-4d94-b902-6663e6008f97	master	f	${role_uma_authorization}	uma_authorization	master	\N	master
990b52cb-5620-40d1-acf8-fe2345766c8c	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_create-client}	create-client	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
86bfc8bb-898f-4bc2-bc94-77026cd1b715	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-realm}	view-realm	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
d8599630-dca7-40e4-bbed-33161339c182	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-users}	view-users	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
c6975a8d-7e0f-4586-ad62-708f1b19649d	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-clients}	view-clients	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
b1148e7b-838e-411d-8ca1-cce658bdca72	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-events}	view-events	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
971d448f-7575-4696-ad11-9de82f02d63d	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-identity-providers}	view-identity-providers	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
ef4e04f8-34ef-4679-b162-6df6ae99be83	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_view-authorization}	view-authorization	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
906a5c1f-a69b-4a3f-ba0a-dab5db2db8e8	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-realm}	manage-realm	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
f6e5f67c-6d32-4a8b-b116-acb38bfd3f32	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-users}	manage-users	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
276a93cc-0d73-4494-99e9-e68c07d7ec81	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-clients}	manage-clients	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
b2f86bac-b7a4-4e4e-86d8-661032b2819e	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-events}	manage-events	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
a6ccf2f7-3768-4c1a-b528-13d95aa65a05	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-identity-providers}	manage-identity-providers	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
654ed8a2-73b7-44fc-80d9-bef55d6c92ff	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_manage-authorization}	manage-authorization	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
87de9812-e3ef-4903-830e-7572f63c63cd	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_query-users}	query-users	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
ab142c47-546c-4522-ac40-3f903026b7ed	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_query-clients}	query-clients	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
296cede5-2e72-4bd2-9e1a-8a93efecccd3	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_query-realms}	query-realms	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
efa5841e-5c6e-46d7-9778-0f2c87b756ec	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_query-groups}	query-groups	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
cb922100-2875-4a8f-86ea-4534de6d8a97	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_realm-admin}	realm-admin	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
eb456567-1eb4-460a-9497-383e20386102	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_create-client}	create-client	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
265e76e9-12c4-4deb-bf74-a5983d2578b4	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-realm}	view-realm	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
dbd38c4c-1454-44b0-a89b-ba25332dc4d3	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-users}	view-users	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
b13f1a28-7a2d-4001-a53d-936340de1b5e	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-clients}	view-clients	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
1abb2ba5-b5a8-4f8b-ac9f-a26c4d27344d	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-events}	view-events	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
d84d5992-a169-4fdd-9b65-fc6d620cea7b	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-identity-providers}	view-identity-providers	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
709b631c-722c-486b-bf95-e0f18c2866b8	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_view-authorization}	view-authorization	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
86e92749-fae4-4600-bb60-46c363b0ad71	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-realm}	manage-realm	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
1fcb60d2-298b-4c5a-bda8-5588ae417f60	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-users}	manage-users	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
470a0f7a-549d-4601-80ea-470f1d6d9994	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-clients}	manage-clients	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
da3eb1e1-8705-46eb-a4f3-4511eb818d71	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-events}	manage-events	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
c3cc344b-77b3-40ae-b78a-5516ba2fca37	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-identity-providers}	manage-identity-providers	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
d261a97f-192c-47bb-8be2-b3db83f5b7e0	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_manage-authorization}	manage-authorization	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
7e32416b-0977-4cf6-a4fc-d7d1d6242b4c	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_query-users}	query-users	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
b3d9b79a-085f-4090-9e3f-8b29a87924ac	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_query-clients}	query-clients	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
9de358c6-ea06-4f1b-8235-8cacb6bb8782	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_query-realms}	query-realms	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
305265b5-8371-4abf-8e71-8207f9c43a8c	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_query-groups}	query-groups	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
04776ef2-69dd-432b-8f78-1753011d1569	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_view-profile}	view-profile	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
cd62b709-9f11-4d60-b4af-270d69efc371	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_manage-account}	manage-account	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
b2543bc1-6378-4bd2-9463-29db8428f994	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_manage-account-links}	manage-account-links	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
b89c9cae-dc06-458a-b71c-80238d16b6df	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_view-applications}	view-applications	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
d108c580-bf94-4155-b971-94b2a4508c4d	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_view-consent}	view-consent	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
20723ea1-e42a-4c9d-a151-cf17c041464c	324d713c-ae08-4f54-8d17-0217a99a1dab	t	${role_manage-consent}	manage-consent	Citygroves	324d713c-ae08-4f54-8d17-0217a99a1dab	\N
70649b4e-f277-48c0-865f-0b7dc62ba18f	7551785f-f1ee-4076-9324-786efa9260b7	t	${role_impersonation}	impersonation	master	7551785f-f1ee-4076-9324-786efa9260b7	\N
15e3d0d9-b6b6-4d96-9dd1-7804118a84c7	e08fe2ab-7a6b-4667-b53c-864db2df766a	t	${role_impersonation}	impersonation	Citygroves	e08fe2ab-7a6b-4667-b53c-864db2df766a	\N
a3a9d25f-534e-40f5-9ec5-42f313072e5f	a5a6a52f-58ff-440a-bc95-690ea7a8871a	t	${role_read-token}	read-token	Citygroves	a5a6a52f-58ff-440a-bc95-690ea7a8871a	\N
70324447-9abb-449c-8d07-4bb22b9643b7	Citygroves	f	${role_offline-access}	offline_access	Citygroves	\N	Citygroves
c9540416-3a72-4343-b373-dfc3e0364968	Citygroves	f	${role_uma_authorization}	uma_authorization	Citygroves	\N	Citygroves
\.


--
-- Data for Name: migration_model; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.migration_model (id, version, update_time) FROM stdin;
uvyg6	9.0.0	1585788715
\.


--
-- Data for Name: offline_client_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.offline_client_session (user_session_id, client_id, offline_flag, "timestamp", data, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: offline_user_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.offline_user_session (user_session_id, user_id, realm_id, created_on, offline_flag, data, last_session_refresh) FROM stdin;
\.


--
-- Data for Name: policy_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.policy_config (policy_id, name, value) FROM stdin;
\.


--
-- Data for Name: protocol_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.protocol_mapper (id, name, protocol, protocol_mapper_name, client_id, client_scope_id) FROM stdin;
bcf25194-38d2-48cd-b450-2c6faa4e6794	audience resolve	openid-connect	oidc-audience-resolve-mapper	6855f198-c04b-4086-9ca5-4b21d8d79b83	\N
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	locale	openid-connect	oidc-usermodel-attribute-mapper	213895bb-cee2-444b-8c09-73ee6428ce92	\N
7c88f938-4923-4b9c-84a5-cda36719cd04	role list	saml	saml-role-list-mapper	\N	952c33c7-6e1a-4166-a2b6-781c4d97c9ad
753e9829-6817-445e-81f9-3baf638b15f9	full name	openid-connect	oidc-full-name-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	family name	openid-connect	oidc-usermodel-property-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
59cfb100-95cd-46b6-b352-9c03cbdce388	given name	openid-connect	oidc-usermodel-property-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
49fbf153-efce-411c-ba62-6db90cad79c2	middle name	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	nickname	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
12ae9177-2af0-4ee6-a8e9-c904d07b656a	username	openid-connect	oidc-usermodel-property-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	profile	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
6f4212bf-e60a-48b0-8d67-38781a24217a	picture	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	website	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
2828df47-0ca5-4e02-96d1-9b69a740a4b3	gender	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	birthdate	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
0ad65db1-cd80-4e50-9e10-975dad291f3b	zoneinfo	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
091b44e1-f3d7-4eb9-acff-392ff4134b47	locale	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
b7f06dfa-b5c4-4e28-a602-56deb7289edc	updated at	openid-connect	oidc-usermodel-attribute-mapper	\N	6fb85823-f6c8-416a-b77d-24f21f73eef3
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	email	openid-connect	oidc-usermodel-property-mapper	\N	a1156a4d-3edf-4e46-8802-dc8f7d071c94
9f425f07-7206-4e77-bfae-2b9d31d140c1	email verified	openid-connect	oidc-usermodel-property-mapper	\N	a1156a4d-3edf-4e46-8802-dc8f7d071c94
00f660ec-b281-4ef8-88c7-b91c62328987	address	openid-connect	oidc-address-mapper	\N	7215e639-b32b-4edc-89fa-109375845473
465bc07f-cc51-413f-88e7-0ca2e6e9360b	phone number	openid-connect	oidc-usermodel-attribute-mapper	\N	af1583de-b675-4dfb-bea4-a3c74d82eaad
cb610fbc-fe10-40f0-ae77-e141400d1cd1	phone number verified	openid-connect	oidc-usermodel-attribute-mapper	\N	af1583de-b675-4dfb-bea4-a3c74d82eaad
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	realm roles	openid-connect	oidc-usermodel-realm-role-mapper	\N	1a5c13e3-16a7-46ca-9833-64dbb4541034
4d453428-6501-44e2-b8e1-81c866aef091	client roles	openid-connect	oidc-usermodel-client-role-mapper	\N	1a5c13e3-16a7-46ca-9833-64dbb4541034
387b741b-7996-49ef-b5ff-98e21f8fe7eb	audience resolve	openid-connect	oidc-audience-resolve-mapper	\N	1a5c13e3-16a7-46ca-9833-64dbb4541034
6aba8183-e5a9-4df7-8f68-4c84afb87521	allowed web origins	openid-connect	oidc-allowed-origins-mapper	\N	1e4543a6-ac19-4298-9722-f555758997f5
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	upn	openid-connect	oidc-usermodel-property-mapper	\N	396a8291-b64d-4f42-8940-14c424b5598c
0696b774-ce61-4167-aaff-59b9f498ccf7	groups	openid-connect	oidc-usermodel-realm-role-mapper	\N	396a8291-b64d-4f42-8940-14c424b5598c
ead9cccb-bad5-47a5-bd91-4d9f639721b2	audience resolve	openid-connect	oidc-audience-resolve-mapper	55b5e24f-bc93-4729-bb0b-849637a9445f	\N
69089f81-15d3-44b4-bc02-3afd75ce19ea	role list	saml	saml-role-list-mapper	\N	b3d82398-6878-4915-a7f1-99ff0ed9a1c0
d21ceb32-a112-4f8f-b984-3077f4748354	full name	openid-connect	oidc-full-name-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	family name	openid-connect	oidc-usermodel-property-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
9d24f288-c00e-449e-acdc-b7d3842a289a	given name	openid-connect	oidc-usermodel-property-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
c8011782-2406-4f89-b66d-1650ba6eee95	middle name	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
8202d2f5-e8cb-4774-9f61-2c120492ca95	nickname	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	username	openid-connect	oidc-usermodel-property-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
eeedabf8-0861-4f3a-a549-37ff160a0d9f	profile	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
f0a95204-f31b-4f27-a7de-de604a19584c	picture	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
7a7a10ee-143d-4dc1-9200-614336ed8d80	website	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
8080e823-5807-4b41-ba15-7ddc0e940fb6	gender	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	birthdate	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
cc57e53e-5c34-4427-94df-5c23d604c080	zoneinfo	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
5c7b658e-4510-4672-89a5-de1facb7fc68	locale	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	updated at	openid-connect	oidc-usermodel-attribute-mapper	\N	fd9416f1-f74e-4c3a-9225-ac6cfab18f2e
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	email	openid-connect	oidc-usermodel-property-mapper	\N	bcb82f70-fd63-4933-829f-183158674f81
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	email verified	openid-connect	oidc-usermodel-property-mapper	\N	bcb82f70-fd63-4933-829f-183158674f81
f4eacc85-02db-49f5-958c-452c9f4d6a31	address	openid-connect	oidc-address-mapper	\N	c9fbc7ca-d340-460d-abee-9c619f8de40c
0974acad-0143-42f1-9913-f718fe6340a0	phone number	openid-connect	oidc-usermodel-attribute-mapper	\N	a72c9669-7fec-43a0-b467-8f2afdc9640d
f8d99cb5-9040-497f-aa20-cd11da457df6	phone number verified	openid-connect	oidc-usermodel-attribute-mapper	\N	a72c9669-7fec-43a0-b467-8f2afdc9640d
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	realm roles	openid-connect	oidc-usermodel-realm-role-mapper	\N	0f29d097-c464-4c81-a65d-304a401d1c96
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	client roles	openid-connect	oidc-usermodel-client-role-mapper	\N	0f29d097-c464-4c81-a65d-304a401d1c96
811334be-318b-4479-8ed5-9077dff800a0	audience resolve	openid-connect	oidc-audience-resolve-mapper	\N	0f29d097-c464-4c81-a65d-304a401d1c96
7fe2d668-eb0b-4aec-a795-384a382b3c72	allowed web origins	openid-connect	oidc-allowed-origins-mapper	\N	bb86f232-3c7e-4409-9de7-c0641a261793
9f454e91-f1f7-4403-8d93-107156814a3d	upn	openid-connect	oidc-usermodel-property-mapper	\N	9b593dbb-eadb-47ec-badb-bcce9ab0c11f
adadff85-262a-4f76-ba2c-8d5d66c0fd87	groups	openid-connect	oidc-usermodel-realm-role-mapper	\N	9b593dbb-eadb-47ec-badb-bcce9ab0c11f
80a54226-ee66-423c-bf1f-a4b3ffaa8394	locale	openid-connect	oidc-usermodel-attribute-mapper	f35244b5-7de5-4c9f-92ea-b34912e69a8a	\N
\.


--
-- Data for Name: protocol_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.protocol_mapper_config (protocol_mapper_id, value, name) FROM stdin;
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	true	userinfo.token.claim
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	locale	user.attribute
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	true	id.token.claim
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	true	access.token.claim
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	locale	claim.name
b463b4c2-5b0d-4ce9-b457-8bd0eb5c5e4d	String	jsonType.label
7c88f938-4923-4b9c-84a5-cda36719cd04	false	single
7c88f938-4923-4b9c-84a5-cda36719cd04	Basic	attribute.nameformat
7c88f938-4923-4b9c-84a5-cda36719cd04	Role	attribute.name
753e9829-6817-445e-81f9-3baf638b15f9	true	userinfo.token.claim
753e9829-6817-445e-81f9-3baf638b15f9	true	id.token.claim
753e9829-6817-445e-81f9-3baf638b15f9	true	access.token.claim
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	true	userinfo.token.claim
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	lastName	user.attribute
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	true	id.token.claim
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	true	access.token.claim
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	family_name	claim.name
1996d5b7-ccd8-4bce-a249-16e3cbb9f873	String	jsonType.label
59cfb100-95cd-46b6-b352-9c03cbdce388	true	userinfo.token.claim
59cfb100-95cd-46b6-b352-9c03cbdce388	firstName	user.attribute
59cfb100-95cd-46b6-b352-9c03cbdce388	true	id.token.claim
59cfb100-95cd-46b6-b352-9c03cbdce388	true	access.token.claim
59cfb100-95cd-46b6-b352-9c03cbdce388	given_name	claim.name
59cfb100-95cd-46b6-b352-9c03cbdce388	String	jsonType.label
49fbf153-efce-411c-ba62-6db90cad79c2	true	userinfo.token.claim
49fbf153-efce-411c-ba62-6db90cad79c2	middleName	user.attribute
49fbf153-efce-411c-ba62-6db90cad79c2	true	id.token.claim
49fbf153-efce-411c-ba62-6db90cad79c2	true	access.token.claim
49fbf153-efce-411c-ba62-6db90cad79c2	middle_name	claim.name
49fbf153-efce-411c-ba62-6db90cad79c2	String	jsonType.label
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	true	userinfo.token.claim
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	nickname	user.attribute
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	true	id.token.claim
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	true	access.token.claim
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	nickname	claim.name
5e149dbb-f8e4-4ee2-ae7f-b7c261cc3729	String	jsonType.label
12ae9177-2af0-4ee6-a8e9-c904d07b656a	true	userinfo.token.claim
12ae9177-2af0-4ee6-a8e9-c904d07b656a	username	user.attribute
12ae9177-2af0-4ee6-a8e9-c904d07b656a	true	id.token.claim
12ae9177-2af0-4ee6-a8e9-c904d07b656a	true	access.token.claim
12ae9177-2af0-4ee6-a8e9-c904d07b656a	preferred_username	claim.name
12ae9177-2af0-4ee6-a8e9-c904d07b656a	String	jsonType.label
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	true	userinfo.token.claim
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	profile	user.attribute
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	true	id.token.claim
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	true	access.token.claim
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	profile	claim.name
607fddf0-6e12-4cf5-8df5-d49be4cdd6fb	String	jsonType.label
6f4212bf-e60a-48b0-8d67-38781a24217a	true	userinfo.token.claim
6f4212bf-e60a-48b0-8d67-38781a24217a	picture	user.attribute
6f4212bf-e60a-48b0-8d67-38781a24217a	true	id.token.claim
6f4212bf-e60a-48b0-8d67-38781a24217a	true	access.token.claim
6f4212bf-e60a-48b0-8d67-38781a24217a	picture	claim.name
6f4212bf-e60a-48b0-8d67-38781a24217a	String	jsonType.label
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	true	userinfo.token.claim
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	website	user.attribute
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	true	id.token.claim
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	true	access.token.claim
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	website	claim.name
a15c2a10-d5a0-4f3b-a292-1e83269e4f68	String	jsonType.label
2828df47-0ca5-4e02-96d1-9b69a740a4b3	true	userinfo.token.claim
2828df47-0ca5-4e02-96d1-9b69a740a4b3	gender	user.attribute
2828df47-0ca5-4e02-96d1-9b69a740a4b3	true	id.token.claim
2828df47-0ca5-4e02-96d1-9b69a740a4b3	true	access.token.claim
2828df47-0ca5-4e02-96d1-9b69a740a4b3	gender	claim.name
2828df47-0ca5-4e02-96d1-9b69a740a4b3	String	jsonType.label
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	true	userinfo.token.claim
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	birthdate	user.attribute
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	true	id.token.claim
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	true	access.token.claim
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	birthdate	claim.name
dbe0bfa6-fd00-4fa4-8417-5b5c3c88cb19	String	jsonType.label
0ad65db1-cd80-4e50-9e10-975dad291f3b	true	userinfo.token.claim
0ad65db1-cd80-4e50-9e10-975dad291f3b	zoneinfo	user.attribute
0ad65db1-cd80-4e50-9e10-975dad291f3b	true	id.token.claim
0ad65db1-cd80-4e50-9e10-975dad291f3b	true	access.token.claim
0ad65db1-cd80-4e50-9e10-975dad291f3b	zoneinfo	claim.name
0ad65db1-cd80-4e50-9e10-975dad291f3b	String	jsonType.label
091b44e1-f3d7-4eb9-acff-392ff4134b47	true	userinfo.token.claim
091b44e1-f3d7-4eb9-acff-392ff4134b47	locale	user.attribute
091b44e1-f3d7-4eb9-acff-392ff4134b47	true	id.token.claim
091b44e1-f3d7-4eb9-acff-392ff4134b47	true	access.token.claim
091b44e1-f3d7-4eb9-acff-392ff4134b47	locale	claim.name
091b44e1-f3d7-4eb9-acff-392ff4134b47	String	jsonType.label
b7f06dfa-b5c4-4e28-a602-56deb7289edc	true	userinfo.token.claim
b7f06dfa-b5c4-4e28-a602-56deb7289edc	updatedAt	user.attribute
b7f06dfa-b5c4-4e28-a602-56deb7289edc	true	id.token.claim
b7f06dfa-b5c4-4e28-a602-56deb7289edc	true	access.token.claim
b7f06dfa-b5c4-4e28-a602-56deb7289edc	updated_at	claim.name
b7f06dfa-b5c4-4e28-a602-56deb7289edc	String	jsonType.label
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	true	userinfo.token.claim
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	email	user.attribute
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	true	id.token.claim
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	true	access.token.claim
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	email	claim.name
8ccb8cdf-e741-4372-8364-ee8f2dfdd56a	String	jsonType.label
9f425f07-7206-4e77-bfae-2b9d31d140c1	true	userinfo.token.claim
9f425f07-7206-4e77-bfae-2b9d31d140c1	emailVerified	user.attribute
9f425f07-7206-4e77-bfae-2b9d31d140c1	true	id.token.claim
9f425f07-7206-4e77-bfae-2b9d31d140c1	true	access.token.claim
9f425f07-7206-4e77-bfae-2b9d31d140c1	email_verified	claim.name
9f425f07-7206-4e77-bfae-2b9d31d140c1	boolean	jsonType.label
00f660ec-b281-4ef8-88c7-b91c62328987	formatted	user.attribute.formatted
00f660ec-b281-4ef8-88c7-b91c62328987	country	user.attribute.country
00f660ec-b281-4ef8-88c7-b91c62328987	postal_code	user.attribute.postal_code
00f660ec-b281-4ef8-88c7-b91c62328987	true	userinfo.token.claim
00f660ec-b281-4ef8-88c7-b91c62328987	street	user.attribute.street
00f660ec-b281-4ef8-88c7-b91c62328987	true	id.token.claim
00f660ec-b281-4ef8-88c7-b91c62328987	region	user.attribute.region
00f660ec-b281-4ef8-88c7-b91c62328987	true	access.token.claim
00f660ec-b281-4ef8-88c7-b91c62328987	locality	user.attribute.locality
465bc07f-cc51-413f-88e7-0ca2e6e9360b	true	userinfo.token.claim
465bc07f-cc51-413f-88e7-0ca2e6e9360b	phoneNumber	user.attribute
465bc07f-cc51-413f-88e7-0ca2e6e9360b	true	id.token.claim
465bc07f-cc51-413f-88e7-0ca2e6e9360b	true	access.token.claim
465bc07f-cc51-413f-88e7-0ca2e6e9360b	phone_number	claim.name
465bc07f-cc51-413f-88e7-0ca2e6e9360b	String	jsonType.label
cb610fbc-fe10-40f0-ae77-e141400d1cd1	true	userinfo.token.claim
cb610fbc-fe10-40f0-ae77-e141400d1cd1	phoneNumberVerified	user.attribute
cb610fbc-fe10-40f0-ae77-e141400d1cd1	true	id.token.claim
cb610fbc-fe10-40f0-ae77-e141400d1cd1	true	access.token.claim
cb610fbc-fe10-40f0-ae77-e141400d1cd1	phone_number_verified	claim.name
cb610fbc-fe10-40f0-ae77-e141400d1cd1	boolean	jsonType.label
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	true	multivalued
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	foo	user.attribute
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	true	access.token.claim
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	realm_access.roles	claim.name
a5accc48-ea7c-425a-94eb-a3ec1a9af3a5	String	jsonType.label
4d453428-6501-44e2-b8e1-81c866aef091	true	multivalued
4d453428-6501-44e2-b8e1-81c866aef091	foo	user.attribute
4d453428-6501-44e2-b8e1-81c866aef091	true	access.token.claim
4d453428-6501-44e2-b8e1-81c866aef091	resource_access.${client_id}.roles	claim.name
4d453428-6501-44e2-b8e1-81c866aef091	String	jsonType.label
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	true	userinfo.token.claim
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	username	user.attribute
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	true	id.token.claim
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	true	access.token.claim
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	upn	claim.name
55ef07c3-84e4-4559-8a53-afb4bf6b54c8	String	jsonType.label
0696b774-ce61-4167-aaff-59b9f498ccf7	true	multivalued
0696b774-ce61-4167-aaff-59b9f498ccf7	foo	user.attribute
0696b774-ce61-4167-aaff-59b9f498ccf7	true	id.token.claim
0696b774-ce61-4167-aaff-59b9f498ccf7	true	access.token.claim
0696b774-ce61-4167-aaff-59b9f498ccf7	groups	claim.name
0696b774-ce61-4167-aaff-59b9f498ccf7	String	jsonType.label
69089f81-15d3-44b4-bc02-3afd75ce19ea	false	single
69089f81-15d3-44b4-bc02-3afd75ce19ea	Basic	attribute.nameformat
69089f81-15d3-44b4-bc02-3afd75ce19ea	Role	attribute.name
d21ceb32-a112-4f8f-b984-3077f4748354	true	userinfo.token.claim
d21ceb32-a112-4f8f-b984-3077f4748354	true	id.token.claim
d21ceb32-a112-4f8f-b984-3077f4748354	true	access.token.claim
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	true	userinfo.token.claim
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	lastName	user.attribute
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	true	id.token.claim
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	true	access.token.claim
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	family_name	claim.name
76a53b6c-5e0e-48b9-9501-cd7fb64a711c	String	jsonType.label
9d24f288-c00e-449e-acdc-b7d3842a289a	true	userinfo.token.claim
9d24f288-c00e-449e-acdc-b7d3842a289a	firstName	user.attribute
9d24f288-c00e-449e-acdc-b7d3842a289a	true	id.token.claim
9d24f288-c00e-449e-acdc-b7d3842a289a	true	access.token.claim
9d24f288-c00e-449e-acdc-b7d3842a289a	given_name	claim.name
9d24f288-c00e-449e-acdc-b7d3842a289a	String	jsonType.label
c8011782-2406-4f89-b66d-1650ba6eee95	true	userinfo.token.claim
c8011782-2406-4f89-b66d-1650ba6eee95	middleName	user.attribute
c8011782-2406-4f89-b66d-1650ba6eee95	true	id.token.claim
c8011782-2406-4f89-b66d-1650ba6eee95	true	access.token.claim
c8011782-2406-4f89-b66d-1650ba6eee95	middle_name	claim.name
c8011782-2406-4f89-b66d-1650ba6eee95	String	jsonType.label
8202d2f5-e8cb-4774-9f61-2c120492ca95	true	userinfo.token.claim
8202d2f5-e8cb-4774-9f61-2c120492ca95	nickname	user.attribute
8202d2f5-e8cb-4774-9f61-2c120492ca95	true	id.token.claim
8202d2f5-e8cb-4774-9f61-2c120492ca95	true	access.token.claim
8202d2f5-e8cb-4774-9f61-2c120492ca95	nickname	claim.name
8202d2f5-e8cb-4774-9f61-2c120492ca95	String	jsonType.label
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	true	userinfo.token.claim
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	username	user.attribute
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	true	id.token.claim
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	true	access.token.claim
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	preferred_username	claim.name
b86f4b9e-321e-4b8f-9e52-e9e5f56b9e93	String	jsonType.label
eeedabf8-0861-4f3a-a549-37ff160a0d9f	true	userinfo.token.claim
eeedabf8-0861-4f3a-a549-37ff160a0d9f	profile	user.attribute
eeedabf8-0861-4f3a-a549-37ff160a0d9f	true	id.token.claim
eeedabf8-0861-4f3a-a549-37ff160a0d9f	true	access.token.claim
eeedabf8-0861-4f3a-a549-37ff160a0d9f	profile	claim.name
eeedabf8-0861-4f3a-a549-37ff160a0d9f	String	jsonType.label
f0a95204-f31b-4f27-a7de-de604a19584c	true	userinfo.token.claim
f0a95204-f31b-4f27-a7de-de604a19584c	picture	user.attribute
f0a95204-f31b-4f27-a7de-de604a19584c	true	id.token.claim
f0a95204-f31b-4f27-a7de-de604a19584c	true	access.token.claim
f0a95204-f31b-4f27-a7de-de604a19584c	picture	claim.name
f0a95204-f31b-4f27-a7de-de604a19584c	String	jsonType.label
7a7a10ee-143d-4dc1-9200-614336ed8d80	true	userinfo.token.claim
7a7a10ee-143d-4dc1-9200-614336ed8d80	website	user.attribute
7a7a10ee-143d-4dc1-9200-614336ed8d80	true	id.token.claim
7a7a10ee-143d-4dc1-9200-614336ed8d80	true	access.token.claim
7a7a10ee-143d-4dc1-9200-614336ed8d80	website	claim.name
7a7a10ee-143d-4dc1-9200-614336ed8d80	String	jsonType.label
8080e823-5807-4b41-ba15-7ddc0e940fb6	true	userinfo.token.claim
8080e823-5807-4b41-ba15-7ddc0e940fb6	gender	user.attribute
8080e823-5807-4b41-ba15-7ddc0e940fb6	true	id.token.claim
8080e823-5807-4b41-ba15-7ddc0e940fb6	true	access.token.claim
8080e823-5807-4b41-ba15-7ddc0e940fb6	gender	claim.name
8080e823-5807-4b41-ba15-7ddc0e940fb6	String	jsonType.label
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	true	userinfo.token.claim
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	birthdate	user.attribute
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	true	id.token.claim
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	true	access.token.claim
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	birthdate	claim.name
466b1aa6-5fde-4a15-a9ca-03ce45ce615f	String	jsonType.label
cc57e53e-5c34-4427-94df-5c23d604c080	true	userinfo.token.claim
cc57e53e-5c34-4427-94df-5c23d604c080	zoneinfo	user.attribute
cc57e53e-5c34-4427-94df-5c23d604c080	true	id.token.claim
cc57e53e-5c34-4427-94df-5c23d604c080	true	access.token.claim
cc57e53e-5c34-4427-94df-5c23d604c080	zoneinfo	claim.name
cc57e53e-5c34-4427-94df-5c23d604c080	String	jsonType.label
5c7b658e-4510-4672-89a5-de1facb7fc68	true	userinfo.token.claim
5c7b658e-4510-4672-89a5-de1facb7fc68	locale	user.attribute
5c7b658e-4510-4672-89a5-de1facb7fc68	true	id.token.claim
5c7b658e-4510-4672-89a5-de1facb7fc68	true	access.token.claim
5c7b658e-4510-4672-89a5-de1facb7fc68	locale	claim.name
5c7b658e-4510-4672-89a5-de1facb7fc68	String	jsonType.label
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	true	userinfo.token.claim
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	updatedAt	user.attribute
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	true	id.token.claim
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	true	access.token.claim
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	updated_at	claim.name
753b175d-0ab8-4b4a-b5b2-3d5fd9a756d8	String	jsonType.label
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	true	userinfo.token.claim
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	email	user.attribute
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	true	id.token.claim
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	true	access.token.claim
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	email	claim.name
9edd2e8e-ce65-4fd4-a57a-139cb8f84073	String	jsonType.label
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	true	userinfo.token.claim
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	emailVerified	user.attribute
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	true	id.token.claim
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	true	access.token.claim
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	email_verified	claim.name
1ea71f9d-50b4-43d6-aec2-88ee24f0eb87	boolean	jsonType.label
f4eacc85-02db-49f5-958c-452c9f4d6a31	formatted	user.attribute.formatted
f4eacc85-02db-49f5-958c-452c9f4d6a31	country	user.attribute.country
f4eacc85-02db-49f5-958c-452c9f4d6a31	postal_code	user.attribute.postal_code
f4eacc85-02db-49f5-958c-452c9f4d6a31	true	userinfo.token.claim
f4eacc85-02db-49f5-958c-452c9f4d6a31	street	user.attribute.street
f4eacc85-02db-49f5-958c-452c9f4d6a31	true	id.token.claim
f4eacc85-02db-49f5-958c-452c9f4d6a31	region	user.attribute.region
f4eacc85-02db-49f5-958c-452c9f4d6a31	true	access.token.claim
f4eacc85-02db-49f5-958c-452c9f4d6a31	locality	user.attribute.locality
0974acad-0143-42f1-9913-f718fe6340a0	true	userinfo.token.claim
0974acad-0143-42f1-9913-f718fe6340a0	phoneNumber	user.attribute
0974acad-0143-42f1-9913-f718fe6340a0	true	id.token.claim
0974acad-0143-42f1-9913-f718fe6340a0	true	access.token.claim
0974acad-0143-42f1-9913-f718fe6340a0	phone_number	claim.name
0974acad-0143-42f1-9913-f718fe6340a0	String	jsonType.label
f8d99cb5-9040-497f-aa20-cd11da457df6	true	userinfo.token.claim
f8d99cb5-9040-497f-aa20-cd11da457df6	phoneNumberVerified	user.attribute
f8d99cb5-9040-497f-aa20-cd11da457df6	true	id.token.claim
f8d99cb5-9040-497f-aa20-cd11da457df6	true	access.token.claim
f8d99cb5-9040-497f-aa20-cd11da457df6	phone_number_verified	claim.name
f8d99cb5-9040-497f-aa20-cd11da457df6	boolean	jsonType.label
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	true	multivalued
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	foo	user.attribute
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	true	access.token.claim
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	realm_access.roles	claim.name
21cb9e44-12c6-44aa-a7ea-435f9dbeebc4	String	jsonType.label
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	true	multivalued
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	foo	user.attribute
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	true	access.token.claim
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	resource_access.${client_id}.roles	claim.name
f65b0dd8-e04b-4c10-9ee3-00b3dc0205d2	String	jsonType.label
9f454e91-f1f7-4403-8d93-107156814a3d	true	userinfo.token.claim
9f454e91-f1f7-4403-8d93-107156814a3d	username	user.attribute
9f454e91-f1f7-4403-8d93-107156814a3d	true	id.token.claim
9f454e91-f1f7-4403-8d93-107156814a3d	true	access.token.claim
9f454e91-f1f7-4403-8d93-107156814a3d	upn	claim.name
9f454e91-f1f7-4403-8d93-107156814a3d	String	jsonType.label
adadff85-262a-4f76-ba2c-8d5d66c0fd87	true	multivalued
adadff85-262a-4f76-ba2c-8d5d66c0fd87	foo	user.attribute
adadff85-262a-4f76-ba2c-8d5d66c0fd87	true	id.token.claim
adadff85-262a-4f76-ba2c-8d5d66c0fd87	true	access.token.claim
adadff85-262a-4f76-ba2c-8d5d66c0fd87	groups	claim.name
adadff85-262a-4f76-ba2c-8d5d66c0fd87	String	jsonType.label
80a54226-ee66-423c-bf1f-a4b3ffaa8394	true	userinfo.token.claim
80a54226-ee66-423c-bf1f-a4b3ffaa8394	locale	user.attribute
80a54226-ee66-423c-bf1f-a4b3ffaa8394	true	id.token.claim
80a54226-ee66-423c-bf1f-a4b3ffaa8394	true	access.token.claim
80a54226-ee66-423c-bf1f-a4b3ffaa8394	locale	claim.name
80a54226-ee66-423c-bf1f-a4b3ffaa8394	String	jsonType.label
\.


--
-- Data for Name: realm; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm (id, access_code_lifespan, user_action_lifespan, access_token_lifespan, account_theme, admin_theme, email_theme, enabled, events_enabled, events_expiration, login_theme, name, not_before, password_policy, registration_allowed, remember_me, reset_password_allowed, social, ssl_required, sso_idle_timeout, sso_max_lifespan, update_profile_on_soc_login, verify_email, master_admin_client, login_lifespan, internationalization_enabled, default_locale, reg_email_as_username, admin_events_enabled, admin_events_details_enabled, edit_username_allowed, otp_policy_counter, otp_policy_window, otp_policy_period, otp_policy_digits, otp_policy_alg, otp_policy_type, browser_flow, registration_flow, direct_grant_flow, reset_credentials_flow, client_auth_flow, offline_session_idle_timeout, revoke_refresh_token, access_token_life_implicit, login_with_email_allowed, duplicate_emails_allowed, docker_auth_flow, refresh_token_max_reuse, allow_user_managed_access, sso_max_lifespan_remember_me, sso_idle_timeout_remember_me) FROM stdin;
Citygroves	60	300	300	\N	\N	\N	t	f	0	\N	Citygroves	0	\N	t	t	t	f	NONE	1800	36000	f	f	7551785f-f1ee-4076-9324-786efa9260b7	1800	f	\N	t	f	f	t	0	1	30	6	HmacSHA1	totp	d2818a82-f1db-4276-86fe-246bc5198e12	e450aca1-68db-4333-8ab0-383861962885	60e1da8c-5e5f-4583-96c4-0be3e745d1a4	e2499a60-4f6d-4a90-99c7-9e95e98e284c	012ef42e-e757-40ce-8652-09a39e56b7d2	2592000	f	900	t	f	2ab8a208-7817-4084-a6d8-741920490f2e	0	f	0	0
master	60	300	60	\N	\N	\N	t	f	0	\N	master	0	\N	f	f	f	f	EXTERNAL	1800	36000	f	f	b1f65320-f3da-48ee-9db1-d5b305f1c855	1800	f	\N	f	f	f	f	0	1	30	6	HmacSHA1	totp	79490408-8ca6-4c72-8065-c1f2979a54ac	05359703-bbea-467e-a919-d195f5b5175c	9884d6b5-d7f9-476b-a97f-52d9fb506768	9bf06127-8c95-49e4-a39f-659f818cde5d	b693e22c-d3f3-4c25-8740-5e9e2c4e94db	2592000	f	900	t	f	4f72d4dd-d825-40a7-91b3-d94247b32937	0	f	0	0
\.


--
-- Data for Name: realm_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_attribute (name, value, realm_id) FROM stdin;
_browser_header.contentSecurityPolicyReportOnly		master
_browser_header.xContentTypeOptions	nosniff	master
_browser_header.xRobotsTag	none	master
_browser_header.xFrameOptions	SAMEORIGIN	master
_browser_header.contentSecurityPolicy	frame-src 'self'; frame-ancestors 'self'; object-src 'none';	master
_browser_header.xXSSProtection	1; mode=block	master
_browser_header.strictTransportSecurity	max-age=31536000; includeSubDomains	master
bruteForceProtected	false	master
permanentLockout	false	master
maxFailureWaitSeconds	900	master
minimumQuickLoginWaitSeconds	60	master
waitIncrementSeconds	60	master
quickLoginCheckMilliSeconds	1000	master
maxDeltaTimeSeconds	43200	master
failureFactor	30	master
displayName	Keycloak	master
displayNameHtml	<div class="kc-logo-text"><span>Keycloak</span></div>	master
offlineSessionMaxLifespanEnabled	false	master
offlineSessionMaxLifespan	5184000	master
_browser_header.contentSecurityPolicyReportOnly		Citygroves
_browser_header.xContentTypeOptions	nosniff	Citygroves
_browser_header.xRobotsTag	none	Citygroves
_browser_header.xFrameOptions	SAMEORIGIN	Citygroves
_browser_header.contentSecurityPolicy	frame-src 'self'; frame-ancestors 'self'; object-src 'none';	Citygroves
_browser_header.xXSSProtection	1; mode=block	Citygroves
_browser_header.strictTransportSecurity	max-age=31536000; includeSubDomains	Citygroves
bruteForceProtected	false	Citygroves
permanentLockout	false	Citygroves
maxFailureWaitSeconds	900	Citygroves
minimumQuickLoginWaitSeconds	60	Citygroves
waitIncrementSeconds	60	Citygroves
quickLoginCheckMilliSeconds	1000	Citygroves
maxDeltaTimeSeconds	43200	Citygroves
failureFactor	30	Citygroves
offlineSessionMaxLifespanEnabled	false	Citygroves
offlineSessionMaxLifespan	5184000	Citygroves
actionTokenGeneratedByAdminLifespan	43200	Citygroves
actionTokenGeneratedByUserLifespan	300	Citygroves
webAuthnPolicyRpEntityName	keycloak	Citygroves
webAuthnPolicySignatureAlgorithms	ES256	Citygroves
webAuthnPolicyRpId		Citygroves
webAuthnPolicyAttestationConveyancePreference	not specified	Citygroves
webAuthnPolicyAuthenticatorAttachment	not specified	Citygroves
webAuthnPolicyRequireResidentKey	not specified	Citygroves
webAuthnPolicyUserVerificationRequirement	not specified	Citygroves
webAuthnPolicyCreateTimeout	0	Citygroves
webAuthnPolicyAvoidSameAuthenticatorRegister	false	Citygroves
webAuthnPolicyRpEntityNamePasswordless	keycloak	Citygroves
webAuthnPolicySignatureAlgorithmsPasswordless	ES256	Citygroves
webAuthnPolicyRpIdPasswordless		Citygroves
webAuthnPolicyAttestationConveyancePreferencePasswordless	not specified	Citygroves
webAuthnPolicyAuthenticatorAttachmentPasswordless	not specified	Citygroves
webAuthnPolicyRequireResidentKeyPasswordless	not specified	Citygroves
webAuthnPolicyUserVerificationRequirementPasswordless	not specified	Citygroves
webAuthnPolicyCreateTimeoutPasswordless	0	Citygroves
webAuthnPolicyAvoidSameAuthenticatorRegisterPasswordless	false	Citygroves
displayName	Citygroves	Citygroves
frontendUrl		Citygroves
\.


--
-- Data for Name: realm_default_groups; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_default_groups (realm_id, group_id) FROM stdin;
\.


--
-- Data for Name: realm_default_roles; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_default_roles (realm_id, role_id) FROM stdin;
master	f6c96cdc-4f19-4bde-bea5-6edef4d84f7a
master	7c2827b5-9734-4d94-b902-6663e6008f97
Citygroves	70324447-9abb-449c-8d07-4bb22b9643b7
Citygroves	c9540416-3a72-4343-b373-dfc3e0364968
\.


--
-- Data for Name: realm_enabled_event_types; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_enabled_event_types (realm_id, value) FROM stdin;
\.


--
-- Data for Name: realm_events_listeners; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_events_listeners (realm_id, value) FROM stdin;
master	jboss-logging
Citygroves	jboss-logging
\.


--
-- Data for Name: realm_required_credential; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_required_credential (type, form_label, input, secret, realm_id) FROM stdin;
password	password	t	t	master
password	password	t	t	Citygroves
\.


--
-- Data for Name: realm_smtp_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_smtp_config (realm_id, value, name) FROM stdin;
\.


--
-- Data for Name: realm_supported_locales; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.realm_supported_locales (realm_id, value) FROM stdin;
\.


--
-- Data for Name: redirect_uris; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.redirect_uris (client_id, value) FROM stdin;
ce09c09e-54bb-4a0a-8b6d-651c069c0361	/realms/master/account/*
6855f198-c04b-4086-9ca5-4b21d8d79b83	/realms/master/account/*
213895bb-cee2-444b-8c09-73ee6428ce92	/admin/master/console/*
324d713c-ae08-4f54-8d17-0217a99a1dab	/realms/Citygroves/account/*
55b5e24f-bc93-4729-bb0b-849637a9445f	/realms/Citygroves/account/*
f35244b5-7de5-4c9f-92ea-b34912e69a8a	/admin/Citygroves/console/*
5b6ce05b-92ae-458b-a01d-80305bf960df	http://citygroves.frontend.local/*
\.


--
-- Data for Name: required_action_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.required_action_config (required_action_id, value, name) FROM stdin;
\.


--
-- Data for Name: required_action_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.required_action_provider (id, alias, name, realm_id, enabled, default_action, provider_id, priority) FROM stdin;
edd138c3-7b20-4695-9e24-5308be274153	VERIFY_EMAIL	Verify Email	master	t	f	VERIFY_EMAIL	50
35c02e0b-c902-4568-b903-77e723d4f768	UPDATE_PROFILE	Update Profile	master	t	f	UPDATE_PROFILE	40
df3abf70-a6f5-49e1-8727-8259e71c2011	CONFIGURE_TOTP	Configure OTP	master	t	f	CONFIGURE_TOTP	10
c4dccce2-1e91-4a4f-a11a-3c5c6970cafd	UPDATE_PASSWORD	Update Password	master	t	f	UPDATE_PASSWORD	30
9f1f33f9-70c5-4a94-8c71-eff416dff57f	terms_and_conditions	Terms and Conditions	master	f	f	terms_and_conditions	20
5b171ab5-feca-4eb9-aa69-aca534dc1c3b	update_user_locale	Update User Locale	master	t	f	update_user_locale	1000
02b4677f-6180-4b06-b4b9-3d2da0807b07	VERIFY_EMAIL	Verify Email	Citygroves	t	f	VERIFY_EMAIL	50
83ba1795-6688-492c-bd61-277651436790	UPDATE_PROFILE	Update Profile	Citygroves	t	f	UPDATE_PROFILE	40
381fcded-e46c-4a9c-82b4-1fd0b77fb533	CONFIGURE_TOTP	Configure OTP	Citygroves	t	f	CONFIGURE_TOTP	10
90a8a5c7-93b3-4ecf-8cb5-463bff4d9dbc	UPDATE_PASSWORD	Update Password	Citygroves	t	f	UPDATE_PASSWORD	30
9c7dd892-9241-4f9e-88a2-ad45858d70f2	terms_and_conditions	Terms and Conditions	Citygroves	f	f	terms_and_conditions	20
2e0e7081-0c09-493a-ab8f-f0440b26b3a7	update_user_locale	Update User Locale	Citygroves	t	f	update_user_locale	1000
\.


--
-- Data for Name: resource_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_attribute (id, name, value, resource_id) FROM stdin;
\.


--
-- Data for Name: resource_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_policy (resource_id, policy_id) FROM stdin;
\.


--
-- Data for Name: resource_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_scope (resource_id, scope_id) FROM stdin;
\.


--
-- Data for Name: resource_server; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server (id, allow_rs_remote_mgmt, policy_enforce_mode, decision_strategy) FROM stdin;
\.


--
-- Data for Name: resource_server_perm_ticket; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_perm_ticket (id, owner, requester, created_timestamp, granted_timestamp, resource_id, scope_id, resource_server_id, policy_id) FROM stdin;
\.


--
-- Data for Name: resource_server_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_policy (id, name, description, type, decision_strategy, logic, resource_server_id, owner) FROM stdin;
\.


--
-- Data for Name: resource_server_resource; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_resource (id, name, type, icon_uri, owner, resource_server_id, owner_managed_access, display_name) FROM stdin;
\.


--
-- Data for Name: resource_server_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_server_scope (id, name, icon_uri, resource_server_id, display_name) FROM stdin;
\.


--
-- Data for Name: resource_uris; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.resource_uris (resource_id, value) FROM stdin;
\.


--
-- Data for Name: role_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.role_attribute (id, role_id, name, value) FROM stdin;
\.


--
-- Data for Name: scope_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.scope_mapping (client_id, role_id) FROM stdin;
6855f198-c04b-4086-9ca5-4b21d8d79b83	68b66fea-396d-4885-bda2-974f6ba5b133
55b5e24f-bc93-4729-bb0b-849637a9445f	cd62b709-9f11-4d60-b4af-270d69efc371
\.


--
-- Data for Name: scope_policy; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.scope_policy (scope_id, policy_id) FROM stdin;
\.


--
-- Data for Name: user_attribute; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_attribute (name, value, user_id, id) FROM stdin;
\.


--
-- Data for Name: user_consent; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_consent (id, client_id, user_id, created_date, last_updated_date, client_storage_provider, external_client_id) FROM stdin;
\.


--
-- Data for Name: user_consent_client_scope; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_consent_client_scope (user_consent_id, scope_id) FROM stdin;
\.


--
-- Data for Name: user_entity; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_entity (id, email, email_constraint, email_verified, enabled, federation_link, first_name, last_name, realm_id, username, created_timestamp, service_account_client_link, not_before) FROM stdin;
b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911	\N	1781e73b-3447-48e9-8a4c-faa3ef3d7cbe	f	t	\N	\N	\N	master	admin	1585788717673	\N	0
b2824e06-27cc-49a7-a767-9b5e37c9d651	test@test.pl	test@test.pl	f	t	\N	Damien	Kwazar	Citygroves	test@test.pl	1585846664677	\N	0
\.


--
-- Data for Name: user_federation_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_config (user_federation_provider_id, value, name) FROM stdin;
\.


--
-- Data for Name: user_federation_mapper; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_mapper (id, name, federation_provider_id, federation_mapper_type, realm_id) FROM stdin;
\.


--
-- Data for Name: user_federation_mapper_config; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_mapper_config (user_federation_mapper_id, value, name) FROM stdin;
\.


--
-- Data for Name: user_federation_provider; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_federation_provider (id, changed_sync_period, display_name, full_sync_period, last_sync, priority, provider_name, realm_id) FROM stdin;
\.


--
-- Data for Name: user_group_membership; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_group_membership (group_id, user_id) FROM stdin;
\.


--
-- Data for Name: user_required_action; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_required_action (user_id, required_action) FROM stdin;
\.


--
-- Data for Name: user_role_mapping; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_role_mapping (role_id, user_id) FROM stdin;
68b66fea-396d-4885-bda2-974f6ba5b133	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911
f6c96cdc-4f19-4bde-bea5-6edef4d84f7a	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911
0e2a4fc9-bc35-4a6f-ac4a-d372f691f5fd	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911
7c2827b5-9734-4d94-b902-6663e6008f97	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911
4ca2b9bd-6be0-4c71-8b7d-473cdb13521b	b5e5f8ed-7d00-4a8b-b9db-fb91f18d0911
c9540416-3a72-4343-b373-dfc3e0364968	b2824e06-27cc-49a7-a767-9b5e37c9d651
04776ef2-69dd-432b-8f78-1753011d1569	b2824e06-27cc-49a7-a767-9b5e37c9d651
cd62b709-9f11-4d60-b4af-270d69efc371	b2824e06-27cc-49a7-a767-9b5e37c9d651
70324447-9abb-449c-8d07-4bb22b9643b7	b2824e06-27cc-49a7-a767-9b5e37c9d651
\.


--
-- Data for Name: user_session; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_session (id, auth_method, ip_address, last_session_refresh, login_username, realm_id, remember_me, started, user_id, user_session_state, broker_session_id, broker_user_id) FROM stdin;
\.


--
-- Data for Name: user_session_note; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.user_session_note (user_session, name, value) FROM stdin;
\.


--
-- Data for Name: username_login_failure; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.username_login_failure (realm_id, username, failed_login_not_before, last_failure, last_ip_failure, num_failures) FROM stdin;
\.


--
-- Data for Name: web_origins; Type: TABLE DATA; Schema: public; Owner: keycloak
--

COPY public.web_origins (client_id, value) FROM stdin;
213895bb-cee2-444b-8c09-73ee6428ce92	+
f35244b5-7de5-4c9f-92ea-b34912e69a8a	+
5b6ce05b-92ae-458b-a01d-80305bf960df	http://citygroves.frontend.local
\.


--
-- Name: username_login_failure CONSTRAINT_17-2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.username_login_failure
    ADD CONSTRAINT "CONSTRAINT_17-2" PRIMARY KEY (realm_id, username);


--
-- Name: keycloak_role UK_J3RWUVD56ONTGSUHOGM184WW2-2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT "UK_J3RWUVD56ONTGSUHOGM184WW2-2" UNIQUE (name, client_realm_constraint);


--
-- Name: client_auth_flow_bindings c_cli_flow_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_auth_flow_bindings
    ADD CONSTRAINT c_cli_flow_bind PRIMARY KEY (client_id, binding_name);


--
-- Name: client_scope_client c_cli_scope_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_client
    ADD CONSTRAINT c_cli_scope_bind PRIMARY KEY (client_id, scope_id);


--
-- Name: client_initial_access cnstr_client_init_acc_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_initial_access
    ADD CONSTRAINT cnstr_client_init_acc_pk PRIMARY KEY (id);


--
-- Name: realm_default_groups con_group_id_def_groups; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT con_group_id_def_groups UNIQUE (group_id);


--
-- Name: broker_link constr_broker_link_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.broker_link
    ADD CONSTRAINT constr_broker_link_pk PRIMARY KEY (identity_provider, user_id);


--
-- Name: client_user_session_note constr_cl_usr_ses_note; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_user_session_note
    ADD CONSTRAINT constr_cl_usr_ses_note PRIMARY KEY (client_session, name);


--
-- Name: client_default_roles constr_client_default_roles; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_default_roles
    ADD CONSTRAINT constr_client_default_roles PRIMARY KEY (client_id, role_id);


--
-- Name: component_config constr_component_config_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component_config
    ADD CONSTRAINT constr_component_config_pk PRIMARY KEY (id);


--
-- Name: component constr_component_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT constr_component_pk PRIMARY KEY (id);


--
-- Name: fed_user_required_action constr_fed_required_action; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_required_action
    ADD CONSTRAINT constr_fed_required_action PRIMARY KEY (required_action, user_id);


--
-- Name: fed_user_attribute constr_fed_user_attr_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_attribute
    ADD CONSTRAINT constr_fed_user_attr_pk PRIMARY KEY (id);


--
-- Name: fed_user_consent constr_fed_user_consent_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_consent
    ADD CONSTRAINT constr_fed_user_consent_pk PRIMARY KEY (id);


--
-- Name: fed_user_credential constr_fed_user_cred_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_credential
    ADD CONSTRAINT constr_fed_user_cred_pk PRIMARY KEY (id);


--
-- Name: fed_user_group_membership constr_fed_user_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_group_membership
    ADD CONSTRAINT constr_fed_user_group PRIMARY KEY (group_id, user_id);


--
-- Name: fed_user_role_mapping constr_fed_user_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_role_mapping
    ADD CONSTRAINT constr_fed_user_role PRIMARY KEY (role_id, user_id);


--
-- Name: federated_user constr_federated_user; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_user
    ADD CONSTRAINT constr_federated_user PRIMARY KEY (id);


--
-- Name: realm_default_groups constr_realm_default_groups; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT constr_realm_default_groups PRIMARY KEY (realm_id, group_id);


--
-- Name: realm_enabled_event_types constr_realm_enabl_event_types; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_enabled_event_types
    ADD CONSTRAINT constr_realm_enabl_event_types PRIMARY KEY (realm_id, value);


--
-- Name: realm_events_listeners constr_realm_events_listeners; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_events_listeners
    ADD CONSTRAINT constr_realm_events_listeners PRIMARY KEY (realm_id, value);


--
-- Name: realm_supported_locales constr_realm_supported_locales; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_supported_locales
    ADD CONSTRAINT constr_realm_supported_locales PRIMARY KEY (realm_id, value);


--
-- Name: identity_provider constraint_2b; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT constraint_2b PRIMARY KEY (internal_id);


--
-- Name: client_attributes constraint_3c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_attributes
    ADD CONSTRAINT constraint_3c PRIMARY KEY (client_id, name);


--
-- Name: event_entity constraint_4; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.event_entity
    ADD CONSTRAINT constraint_4 PRIMARY KEY (id);


--
-- Name: federated_identity constraint_40; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_identity
    ADD CONSTRAINT constraint_40 PRIMARY KEY (identity_provider, user_id);


--
-- Name: realm constraint_4a; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm
    ADD CONSTRAINT constraint_4a PRIMARY KEY (id);


--
-- Name: client_session_role constraint_5; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_role
    ADD CONSTRAINT constraint_5 PRIMARY KEY (client_session, role_id);


--
-- Name: user_session constraint_57; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session
    ADD CONSTRAINT constraint_57 PRIMARY KEY (id);


--
-- Name: user_federation_provider constraint_5c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_provider
    ADD CONSTRAINT constraint_5c PRIMARY KEY (id);


--
-- Name: client_session_note constraint_5e; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_note
    ADD CONSTRAINT constraint_5e PRIMARY KEY (client_session, name);


--
-- Name: client constraint_7; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT constraint_7 PRIMARY KEY (id);


--
-- Name: client_session constraint_8; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session
    ADD CONSTRAINT constraint_8 PRIMARY KEY (id);


--
-- Name: scope_mapping constraint_81; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_mapping
    ADD CONSTRAINT constraint_81 PRIMARY KEY (client_id, role_id);


--
-- Name: client_node_registrations constraint_84; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_node_registrations
    ADD CONSTRAINT constraint_84 PRIMARY KEY (client_id, name);


--
-- Name: realm_attribute constraint_9; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_attribute
    ADD CONSTRAINT constraint_9 PRIMARY KEY (name, realm_id);


--
-- Name: realm_required_credential constraint_92; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_required_credential
    ADD CONSTRAINT constraint_92 PRIMARY KEY (realm_id, type);


--
-- Name: keycloak_role constraint_a; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT constraint_a PRIMARY KEY (id);


--
-- Name: admin_event_entity constraint_admin_event_entity; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.admin_event_entity
    ADD CONSTRAINT constraint_admin_event_entity PRIMARY KEY (id);


--
-- Name: authenticator_config_entry constraint_auth_cfg_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config_entry
    ADD CONSTRAINT constraint_auth_cfg_pk PRIMARY KEY (authenticator_id, name);


--
-- Name: authentication_execution constraint_auth_exec_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT constraint_auth_exec_pk PRIMARY KEY (id);


--
-- Name: authentication_flow constraint_auth_flow_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_flow
    ADD CONSTRAINT constraint_auth_flow_pk PRIMARY KEY (id);


--
-- Name: authenticator_config constraint_auth_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config
    ADD CONSTRAINT constraint_auth_pk PRIMARY KEY (id);


--
-- Name: client_session_auth_status constraint_auth_status_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_auth_status
    ADD CONSTRAINT constraint_auth_status_pk PRIMARY KEY (client_session, authenticator);


--
-- Name: user_role_mapping constraint_c; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_role_mapping
    ADD CONSTRAINT constraint_c PRIMARY KEY (role_id, user_id);


--
-- Name: composite_role constraint_composite_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT constraint_composite_role PRIMARY KEY (composite, child_role);


--
-- Name: client_session_prot_mapper constraint_cs_pmp_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_prot_mapper
    ADD CONSTRAINT constraint_cs_pmp_pk PRIMARY KEY (client_session, protocol_mapper_id);


--
-- Name: identity_provider_config constraint_d; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_config
    ADD CONSTRAINT constraint_d PRIMARY KEY (identity_provider_id, name);


--
-- Name: policy_config constraint_dpc; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.policy_config
    ADD CONSTRAINT constraint_dpc PRIMARY KEY (policy_id, name);


--
-- Name: realm_smtp_config constraint_e; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_smtp_config
    ADD CONSTRAINT constraint_e PRIMARY KEY (realm_id, name);


--
-- Name: credential constraint_f; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.credential
    ADD CONSTRAINT constraint_f PRIMARY KEY (id);


--
-- Name: user_federation_config constraint_f9; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_config
    ADD CONSTRAINT constraint_f9 PRIMARY KEY (user_federation_provider_id, name);


--
-- Name: resource_server_perm_ticket constraint_fapmt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT constraint_fapmt PRIMARY KEY (id);


--
-- Name: resource_server_resource constraint_farsr; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT constraint_farsr PRIMARY KEY (id);


--
-- Name: resource_server_policy constraint_farsrp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT constraint_farsrp PRIMARY KEY (id);


--
-- Name: associated_policy constraint_farsrpap; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT constraint_farsrpap PRIMARY KEY (policy_id, associated_policy_id);


--
-- Name: resource_policy constraint_farsrpp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT constraint_farsrpp PRIMARY KEY (resource_id, policy_id);


--
-- Name: resource_server_scope constraint_farsrs; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT constraint_farsrs PRIMARY KEY (id);


--
-- Name: resource_scope constraint_farsrsp; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT constraint_farsrsp PRIMARY KEY (resource_id, scope_id);


--
-- Name: scope_policy constraint_farsrsps; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT constraint_farsrsps PRIMARY KEY (scope_id, policy_id);


--
-- Name: user_entity constraint_fb; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT constraint_fb PRIMARY KEY (id);


--
-- Name: user_federation_mapper_config constraint_fedmapper_cfg_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper_config
    ADD CONSTRAINT constraint_fedmapper_cfg_pm PRIMARY KEY (user_federation_mapper_id, name);


--
-- Name: user_federation_mapper constraint_fedmapperpm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT constraint_fedmapperpm PRIMARY KEY (id);


--
-- Name: fed_user_consent_cl_scope constraint_fgrntcsnt_clsc_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.fed_user_consent_cl_scope
    ADD CONSTRAINT constraint_fgrntcsnt_clsc_pm PRIMARY KEY (user_consent_id, scope_id);


--
-- Name: user_consent_client_scope constraint_grntcsnt_clsc_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent_client_scope
    ADD CONSTRAINT constraint_grntcsnt_clsc_pm PRIMARY KEY (user_consent_id, scope_id);


--
-- Name: user_consent constraint_grntcsnt_pm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT constraint_grntcsnt_pm PRIMARY KEY (id);


--
-- Name: keycloak_group constraint_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_group
    ADD CONSTRAINT constraint_group PRIMARY KEY (id);


--
-- Name: group_attribute constraint_group_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_attribute
    ADD CONSTRAINT constraint_group_attribute_pk PRIMARY KEY (id);


--
-- Name: group_role_mapping constraint_group_role; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_role_mapping
    ADD CONSTRAINT constraint_group_role PRIMARY KEY (role_id, group_id);


--
-- Name: identity_provider_mapper constraint_idpm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_mapper
    ADD CONSTRAINT constraint_idpm PRIMARY KEY (id);


--
-- Name: idp_mapper_config constraint_idpmconfig; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.idp_mapper_config
    ADD CONSTRAINT constraint_idpmconfig PRIMARY KEY (idp_mapper_id, name);


--
-- Name: migration_model constraint_migmod; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.migration_model
    ADD CONSTRAINT constraint_migmod PRIMARY KEY (id);


--
-- Name: offline_client_session constraint_offl_cl_ses_pk3; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.offline_client_session
    ADD CONSTRAINT constraint_offl_cl_ses_pk3 PRIMARY KEY (user_session_id, client_id, client_storage_provider, external_client_id, offline_flag);


--
-- Name: offline_user_session constraint_offl_us_ses_pk2; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.offline_user_session
    ADD CONSTRAINT constraint_offl_us_ses_pk2 PRIMARY KEY (user_session_id, offline_flag);


--
-- Name: protocol_mapper constraint_pcm; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT constraint_pcm PRIMARY KEY (id);


--
-- Name: protocol_mapper_config constraint_pmconfig; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper_config
    ADD CONSTRAINT constraint_pmconfig PRIMARY KEY (protocol_mapper_id, name);


--
-- Name: realm_default_roles constraint_realm_default_roles; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_roles
    ADD CONSTRAINT constraint_realm_default_roles PRIMARY KEY (realm_id, role_id);


--
-- Name: redirect_uris constraint_redirect_uris; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.redirect_uris
    ADD CONSTRAINT constraint_redirect_uris PRIMARY KEY (client_id, value);


--
-- Name: required_action_config constraint_req_act_cfg_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_config
    ADD CONSTRAINT constraint_req_act_cfg_pk PRIMARY KEY (required_action_id, name);


--
-- Name: required_action_provider constraint_req_act_prv_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_provider
    ADD CONSTRAINT constraint_req_act_prv_pk PRIMARY KEY (id);


--
-- Name: user_required_action constraint_required_action; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_required_action
    ADD CONSTRAINT constraint_required_action PRIMARY KEY (required_action, user_id);


--
-- Name: resource_uris constraint_resour_uris_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_uris
    ADD CONSTRAINT constraint_resour_uris_pk PRIMARY KEY (resource_id, value);


--
-- Name: role_attribute constraint_role_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.role_attribute
    ADD CONSTRAINT constraint_role_attribute_pk PRIMARY KEY (id);


--
-- Name: user_attribute constraint_user_attribute_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_attribute
    ADD CONSTRAINT constraint_user_attribute_pk PRIMARY KEY (id);


--
-- Name: user_group_membership constraint_user_group; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_group_membership
    ADD CONSTRAINT constraint_user_group PRIMARY KEY (group_id, user_id);


--
-- Name: user_session_note constraint_usn_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session_note
    ADD CONSTRAINT constraint_usn_pk PRIMARY KEY (user_session, name);


--
-- Name: web_origins constraint_web_origins; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.web_origins
    ADD CONSTRAINT constraint_web_origins PRIMARY KEY (client_id, value);


--
-- Name: client_scope_attributes pk_cl_tmpl_attr; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_attributes
    ADD CONSTRAINT pk_cl_tmpl_attr PRIMARY KEY (scope_id, name);


--
-- Name: client_scope pk_cli_template; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope
    ADD CONSTRAINT pk_cli_template PRIMARY KEY (id);


--
-- Name: databasechangeloglock pk_databasechangeloglock; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.databasechangeloglock
    ADD CONSTRAINT pk_databasechangeloglock PRIMARY KEY (id);


--
-- Name: resource_server pk_resource_server; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server
    ADD CONSTRAINT pk_resource_server PRIMARY KEY (id);


--
-- Name: client_scope_role_mapping pk_template_scope; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_role_mapping
    ADD CONSTRAINT pk_template_scope PRIMARY KEY (scope_id, role_id);


--
-- Name: default_client_scope r_def_cli_scope_bind; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.default_client_scope
    ADD CONSTRAINT r_def_cli_scope_bind PRIMARY KEY (realm_id, scope_id);


--
-- Name: resource_attribute res_attr_pk; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_attribute
    ADD CONSTRAINT res_attr_pk PRIMARY KEY (id);


--
-- Name: keycloak_group sibling_names; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_group
    ADD CONSTRAINT sibling_names UNIQUE (realm_id, parent_group, name);


--
-- Name: identity_provider uk_2daelwnibji49avxsrtuf6xj33; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT uk_2daelwnibji49avxsrtuf6xj33 UNIQUE (provider_alias, realm_id);


--
-- Name: client_default_roles uk_8aelwnibji49avxsrtuf6xjow; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_default_roles
    ADD CONSTRAINT uk_8aelwnibji49avxsrtuf6xjow UNIQUE (role_id);


--
-- Name: client uk_b71cjlbenv945rb6gcon438at; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT uk_b71cjlbenv945rb6gcon438at UNIQUE (realm_id, client_id);


--
-- Name: client_scope uk_cli_scope; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope
    ADD CONSTRAINT uk_cli_scope UNIQUE (realm_id, name);


--
-- Name: user_entity uk_dykn684sl8up1crfei6eckhd7; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT uk_dykn684sl8up1crfei6eckhd7 UNIQUE (realm_id, email_constraint);


--
-- Name: resource_server_resource uk_frsr6t700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT uk_frsr6t700s9v50bu18ws5ha6 UNIQUE (name, owner, resource_server_id);


--
-- Name: resource_server_perm_ticket uk_frsr6t700s9v50bu18ws5pmt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT uk_frsr6t700s9v50bu18ws5pmt UNIQUE (owner, requester, resource_server_id, resource_id, scope_id);


--
-- Name: resource_server_policy uk_frsrpt700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT uk_frsrpt700s9v50bu18ws5ha6 UNIQUE (name, resource_server_id);


--
-- Name: resource_server_scope uk_frsrst700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT uk_frsrst700s9v50bu18ws5ha6 UNIQUE (name, resource_server_id);


--
-- Name: realm_default_roles uk_h4wpd7w4hsoolni3h0sw7btje; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_roles
    ADD CONSTRAINT uk_h4wpd7w4hsoolni3h0sw7btje UNIQUE (role_id);


--
-- Name: user_consent uk_jkuwuvd56ontgsuhogm8uewrt; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT uk_jkuwuvd56ontgsuhogm8uewrt UNIQUE (client_id, client_storage_provider, external_client_id, user_id);


--
-- Name: realm uk_orvsdmla56612eaefiq6wl5oi; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm
    ADD CONSTRAINT uk_orvsdmla56612eaefiq6wl5oi UNIQUE (name);


--
-- Name: user_entity uk_ru8tt6t700s9v50bu18ws5ha6; Type: CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_entity
    ADD CONSTRAINT uk_ru8tt6t700s9v50bu18ws5ha6 UNIQUE (realm_id, username);


--
-- Name: idx_assoc_pol_assoc_pol_id; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_assoc_pol_assoc_pol_id ON public.associated_policy USING btree (associated_policy_id);


--
-- Name: idx_auth_config_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_config_realm ON public.authenticator_config USING btree (realm_id);


--
-- Name: idx_auth_exec_flow; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_exec_flow ON public.authentication_execution USING btree (flow_id);


--
-- Name: idx_auth_exec_realm_flow; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_exec_realm_flow ON public.authentication_execution USING btree (realm_id, flow_id);


--
-- Name: idx_auth_flow_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_auth_flow_realm ON public.authentication_flow USING btree (realm_id);


--
-- Name: idx_cl_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_cl_clscope ON public.client_scope_client USING btree (scope_id);


--
-- Name: idx_client_def_roles_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_def_roles_client ON public.client_default_roles USING btree (client_id);


--
-- Name: idx_client_init_acc_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_init_acc_realm ON public.client_initial_access USING btree (realm_id);


--
-- Name: idx_client_session_session; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_client_session_session ON public.client_session USING btree (session_id);


--
-- Name: idx_clscope_attrs; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_attrs ON public.client_scope_attributes USING btree (scope_id);


--
-- Name: idx_clscope_cl; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_cl ON public.client_scope_client USING btree (client_id);


--
-- Name: idx_clscope_protmap; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_protmap ON public.protocol_mapper USING btree (client_scope_id);


--
-- Name: idx_clscope_role; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_clscope_role ON public.client_scope_role_mapping USING btree (scope_id);


--
-- Name: idx_compo_config_compo; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_compo_config_compo ON public.component_config USING btree (component_id);


--
-- Name: idx_component_provider_type; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_component_provider_type ON public.component USING btree (provider_type);


--
-- Name: idx_component_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_component_realm ON public.component USING btree (realm_id);


--
-- Name: idx_composite; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_composite ON public.composite_role USING btree (composite);


--
-- Name: idx_composite_child; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_composite_child ON public.composite_role USING btree (child_role);


--
-- Name: idx_defcls_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_defcls_realm ON public.default_client_scope USING btree (realm_id);


--
-- Name: idx_defcls_scope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_defcls_scope ON public.default_client_scope USING btree (scope_id);


--
-- Name: idx_fedidentity_feduser; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fedidentity_feduser ON public.federated_identity USING btree (federated_user_id);


--
-- Name: idx_fedidentity_user; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fedidentity_user ON public.federated_identity USING btree (user_id);


--
-- Name: idx_fu_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_attribute ON public.fed_user_attribute USING btree (user_id, realm_id, name);


--
-- Name: idx_fu_cnsnt_ext; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_cnsnt_ext ON public.fed_user_consent USING btree (user_id, client_storage_provider, external_client_id);


--
-- Name: idx_fu_consent; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_consent ON public.fed_user_consent USING btree (user_id, client_id);


--
-- Name: idx_fu_consent_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_consent_ru ON public.fed_user_consent USING btree (realm_id, user_id);


--
-- Name: idx_fu_credential; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_credential ON public.fed_user_credential USING btree (user_id, type);


--
-- Name: idx_fu_credential_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_credential_ru ON public.fed_user_credential USING btree (realm_id, user_id);


--
-- Name: idx_fu_group_membership; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_group_membership ON public.fed_user_group_membership USING btree (user_id, group_id);


--
-- Name: idx_fu_group_membership_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_group_membership_ru ON public.fed_user_group_membership USING btree (realm_id, user_id);


--
-- Name: idx_fu_required_action; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_required_action ON public.fed_user_required_action USING btree (user_id, required_action);


--
-- Name: idx_fu_required_action_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_required_action_ru ON public.fed_user_required_action USING btree (realm_id, user_id);


--
-- Name: idx_fu_role_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_role_mapping ON public.fed_user_role_mapping USING btree (user_id, role_id);


--
-- Name: idx_fu_role_mapping_ru; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_fu_role_mapping_ru ON public.fed_user_role_mapping USING btree (realm_id, user_id);


--
-- Name: idx_group_attr_group; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_group_attr_group ON public.group_attribute USING btree (group_id);


--
-- Name: idx_group_role_mapp_group; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_group_role_mapp_group ON public.group_role_mapping USING btree (group_id);


--
-- Name: idx_id_prov_mapp_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_id_prov_mapp_realm ON public.identity_provider_mapper USING btree (realm_id);


--
-- Name: idx_ident_prov_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_ident_prov_realm ON public.identity_provider USING btree (realm_id);


--
-- Name: idx_keycloak_role_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_keycloak_role_client ON public.keycloak_role USING btree (client);


--
-- Name: idx_keycloak_role_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_keycloak_role_realm ON public.keycloak_role USING btree (realm);


--
-- Name: idx_offline_uss_createdon; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_offline_uss_createdon ON public.offline_user_session USING btree (created_on);


--
-- Name: idx_protocol_mapper_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_protocol_mapper_client ON public.protocol_mapper USING btree (client_id);


--
-- Name: idx_realm_attr_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_attr_realm ON public.realm_attribute USING btree (realm_id);


--
-- Name: idx_realm_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_clscope ON public.client_scope USING btree (realm_id);


--
-- Name: idx_realm_def_grp_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_def_grp_realm ON public.realm_default_groups USING btree (realm_id);


--
-- Name: idx_realm_def_roles_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_def_roles_realm ON public.realm_default_roles USING btree (realm_id);


--
-- Name: idx_realm_evt_list_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_evt_list_realm ON public.realm_events_listeners USING btree (realm_id);


--
-- Name: idx_realm_evt_types_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_evt_types_realm ON public.realm_enabled_event_types USING btree (realm_id);


--
-- Name: idx_realm_master_adm_cli; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_master_adm_cli ON public.realm USING btree (master_admin_client);


--
-- Name: idx_realm_supp_local_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_realm_supp_local_realm ON public.realm_supported_locales USING btree (realm_id);


--
-- Name: idx_redir_uri_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_redir_uri_client ON public.redirect_uris USING btree (client_id);


--
-- Name: idx_req_act_prov_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_req_act_prov_realm ON public.required_action_provider USING btree (realm_id);


--
-- Name: idx_res_policy_policy; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_policy_policy ON public.resource_policy USING btree (policy_id);


--
-- Name: idx_res_scope_scope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_scope_scope ON public.resource_scope USING btree (scope_id);


--
-- Name: idx_res_serv_pol_res_serv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_serv_pol_res_serv ON public.resource_server_policy USING btree (resource_server_id);


--
-- Name: idx_res_srv_res_res_srv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_srv_res_res_srv ON public.resource_server_resource USING btree (resource_server_id);


--
-- Name: idx_res_srv_scope_res_srv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_res_srv_scope_res_srv ON public.resource_server_scope USING btree (resource_server_id);


--
-- Name: idx_role_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_role_attribute ON public.role_attribute USING btree (role_id);


--
-- Name: idx_role_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_role_clscope ON public.client_scope_role_mapping USING btree (role_id);


--
-- Name: idx_scope_mapping_role; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_scope_mapping_role ON public.scope_mapping USING btree (role_id);


--
-- Name: idx_scope_policy_policy; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_scope_policy_policy ON public.scope_policy USING btree (policy_id);


--
-- Name: idx_update_time; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_update_time ON public.migration_model USING btree (update_time);


--
-- Name: idx_us_sess_id_on_cl_sess; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_us_sess_id_on_cl_sess ON public.offline_client_session USING btree (user_session_id);


--
-- Name: idx_usconsent_clscope; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usconsent_clscope ON public.user_consent_client_scope USING btree (user_consent_id);


--
-- Name: idx_user_attribute; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_attribute ON public.user_attribute USING btree (user_id);


--
-- Name: idx_user_consent; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_consent ON public.user_consent USING btree (user_id);


--
-- Name: idx_user_credential; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_credential ON public.credential USING btree (user_id);


--
-- Name: idx_user_email; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_email ON public.user_entity USING btree (email);


--
-- Name: idx_user_group_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_group_mapping ON public.user_group_membership USING btree (user_id);


--
-- Name: idx_user_reqactions; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_reqactions ON public.user_required_action USING btree (user_id);


--
-- Name: idx_user_role_mapping; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_user_role_mapping ON public.user_role_mapping USING btree (user_id);


--
-- Name: idx_usr_fed_map_fed_prv; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_map_fed_prv ON public.user_federation_mapper USING btree (federation_provider_id);


--
-- Name: idx_usr_fed_map_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_map_realm ON public.user_federation_mapper USING btree (realm_id);


--
-- Name: idx_usr_fed_prv_realm; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_usr_fed_prv_realm ON public.user_federation_provider USING btree (realm_id);


--
-- Name: idx_web_orig_client; Type: INDEX; Schema: public; Owner: keycloak
--

CREATE INDEX idx_web_orig_client ON public.web_origins USING btree (client_id);


--
-- Name: client_session_auth_status auth_status_constraint; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_auth_status
    ADD CONSTRAINT auth_status_constraint FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: identity_provider fk2b4ebc52ae5c3b34; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider
    ADD CONSTRAINT fk2b4ebc52ae5c3b34 FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_attributes fk3c47c64beacca966; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_attributes
    ADD CONSTRAINT fk3c47c64beacca966 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: federated_identity fk404288b92ef007a6; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.federated_identity
    ADD CONSTRAINT fk404288b92ef007a6 FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: client_node_registrations fk4129723ba992f594; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_node_registrations
    ADD CONSTRAINT fk4129723ba992f594 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: client_session_note fk5edfb00ff51c2736; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_note
    ADD CONSTRAINT fk5edfb00ff51c2736 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: user_session_note fk5edfb00ff51d3472; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_session_note
    ADD CONSTRAINT fk5edfb00ff51d3472 FOREIGN KEY (user_session) REFERENCES public.user_session(id);


--
-- Name: client_session_role fk_11b7sgqw18i532811v7o2dv76; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_role
    ADD CONSTRAINT fk_11b7sgqw18i532811v7o2dv76 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: redirect_uris fk_1burs8pb4ouj97h5wuppahv9f; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.redirect_uris
    ADD CONSTRAINT fk_1burs8pb4ouj97h5wuppahv9f FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: user_federation_provider fk_1fj32f6ptolw2qy60cd8n01e8; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_provider
    ADD CONSTRAINT fk_1fj32f6ptolw2qy60cd8n01e8 FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_session_prot_mapper fk_33a8sgqw18i532811v7o2dk89; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session_prot_mapper
    ADD CONSTRAINT fk_33a8sgqw18i532811v7o2dk89 FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: realm_required_credential fk_5hg65lybevavkqfki3kponh9v; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_required_credential
    ADD CONSTRAINT fk_5hg65lybevavkqfki3kponh9v FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: resource_attribute fk_5hrm2vlf9ql5fu022kqepovbr; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_attribute
    ADD CONSTRAINT fk_5hrm2vlf9ql5fu022kqepovbr FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: user_attribute fk_5hrm2vlf9ql5fu043kqepovbr; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_attribute
    ADD CONSTRAINT fk_5hrm2vlf9ql5fu043kqepovbr FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: user_required_action fk_6qj3w1jw9cvafhe19bwsiuvmd; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_required_action
    ADD CONSTRAINT fk_6qj3w1jw9cvafhe19bwsiuvmd FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: keycloak_role fk_6vyqfe4cn4wlq8r6kt5vdsj5c; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT fk_6vyqfe4cn4wlq8r6kt5vdsj5c FOREIGN KEY (realm) REFERENCES public.realm(id);


--
-- Name: realm_smtp_config fk_70ej8xdxgxd0b9hh6180irr0o; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_smtp_config
    ADD CONSTRAINT fk_70ej8xdxgxd0b9hh6180irr0o FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_default_roles fk_8aelwnibji49avxsrtuf6xjow; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_default_roles
    ADD CONSTRAINT fk_8aelwnibji49avxsrtuf6xjow FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: realm_attribute fk_8shxd6l3e9atqukacxgpffptw; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_attribute
    ADD CONSTRAINT fk_8shxd6l3e9atqukacxgpffptw FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: composite_role fk_a63wvekftu8jo1pnj81e7mce2; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT fk_a63wvekftu8jo1pnj81e7mce2 FOREIGN KEY (composite) REFERENCES public.keycloak_role(id);


--
-- Name: authentication_execution fk_auth_exec_flow; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT fk_auth_exec_flow FOREIGN KEY (flow_id) REFERENCES public.authentication_flow(id);


--
-- Name: authentication_execution fk_auth_exec_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_execution
    ADD CONSTRAINT fk_auth_exec_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: authentication_flow fk_auth_flow_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authentication_flow
    ADD CONSTRAINT fk_auth_flow_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: authenticator_config fk_auth_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.authenticator_config
    ADD CONSTRAINT fk_auth_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: client_session fk_b4ao2vcvat6ukau74wbwtfqo1; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_session
    ADD CONSTRAINT fk_b4ao2vcvat6ukau74wbwtfqo1 FOREIGN KEY (session_id) REFERENCES public.user_session(id);


--
-- Name: user_role_mapping fk_c4fqv34p1mbylloxang7b1q3l; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_role_mapping
    ADD CONSTRAINT fk_c4fqv34p1mbylloxang7b1q3l FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: client_scope_client fk_c_cli_scope_client; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_client
    ADD CONSTRAINT fk_c_cli_scope_client FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: client_scope_client fk_c_cli_scope_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_client
    ADD CONSTRAINT fk_c_cli_scope_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_scope_attributes fk_cl_scope_attr_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_attributes
    ADD CONSTRAINT fk_cl_scope_attr_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_scope_role_mapping fk_cl_scope_rm_role; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_role_mapping
    ADD CONSTRAINT fk_cl_scope_rm_role FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: client_scope_role_mapping fk_cl_scope_rm_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope_role_mapping
    ADD CONSTRAINT fk_cl_scope_rm_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_user_session_note fk_cl_usr_ses_note; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_user_session_note
    ADD CONSTRAINT fk_cl_usr_ses_note FOREIGN KEY (client_session) REFERENCES public.client_session(id);


--
-- Name: protocol_mapper fk_cli_scope_mapper; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT fk_cli_scope_mapper FOREIGN KEY (client_scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_initial_access fk_client_init_acc_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_initial_access
    ADD CONSTRAINT fk_client_init_acc_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: component_config fk_component_config; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component_config
    ADD CONSTRAINT fk_component_config FOREIGN KEY (component_id) REFERENCES public.component(id);


--
-- Name: component fk_component_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.component
    ADD CONSTRAINT fk_component_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_default_groups fk_def_groups_group; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT fk_def_groups_group FOREIGN KEY (group_id) REFERENCES public.keycloak_group(id);


--
-- Name: realm_default_groups fk_def_groups_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_groups
    ADD CONSTRAINT fk_def_groups_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_default_roles fk_evudb1ppw84oxfax2drs03icc; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_roles
    ADD CONSTRAINT fk_evudb1ppw84oxfax2drs03icc FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: user_federation_mapper_config fk_fedmapper_cfg; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper_config
    ADD CONSTRAINT fk_fedmapper_cfg FOREIGN KEY (user_federation_mapper_id) REFERENCES public.user_federation_mapper(id);


--
-- Name: user_federation_mapper fk_fedmapperpm_fedprv; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT fk_fedmapperpm_fedprv FOREIGN KEY (federation_provider_id) REFERENCES public.user_federation_provider(id);


--
-- Name: user_federation_mapper fk_fedmapperpm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_mapper
    ADD CONSTRAINT fk_fedmapperpm_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: associated_policy fk_frsr5s213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT fk_frsr5s213xcx4wnkog82ssrfy FOREIGN KEY (associated_policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: scope_policy fk_frsrasp13xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT fk_frsrasp13xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog82sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog82sspmt FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_server_resource fk_frsrho213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_resource
    ADD CONSTRAINT fk_frsrho213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog83sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog83sspmt FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_server_perm_ticket fk_frsrho213xcx4wnkog84sspmt; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrho213xcx4wnkog84sspmt FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: associated_policy fk_frsrpas14xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.associated_policy
    ADD CONSTRAINT fk_frsrpas14xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: scope_policy fk_frsrpass3xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_policy
    ADD CONSTRAINT fk_frsrpass3xcx4wnkog82ssrfy FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: resource_server_perm_ticket fk_frsrpo2128cx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_perm_ticket
    ADD CONSTRAINT fk_frsrpo2128cx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_server_policy fk_frsrpo213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_policy
    ADD CONSTRAINT fk_frsrpo213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: resource_scope fk_frsrpos13xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT fk_frsrpos13xcx4wnkog82ssrfy FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_policy fk_frsrpos53xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT fk_frsrpos53xcx4wnkog82ssrfy FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: resource_policy fk_frsrpp213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_policy
    ADD CONSTRAINT fk_frsrpp213xcx4wnkog82ssrfy FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: resource_scope fk_frsrps213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_scope
    ADD CONSTRAINT fk_frsrps213xcx4wnkog82ssrfy FOREIGN KEY (scope_id) REFERENCES public.resource_server_scope(id);


--
-- Name: resource_server_scope fk_frsrso213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_server_scope
    ADD CONSTRAINT fk_frsrso213xcx4wnkog82ssrfy FOREIGN KEY (resource_server_id) REFERENCES public.resource_server(id);


--
-- Name: composite_role fk_gr7thllb9lu8q4vqa4524jjy8; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.composite_role
    ADD CONSTRAINT fk_gr7thllb9lu8q4vqa4524jjy8 FOREIGN KEY (child_role) REFERENCES public.keycloak_role(id);


--
-- Name: user_consent_client_scope fk_grntcsnt_clsc_usc; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent_client_scope
    ADD CONSTRAINT fk_grntcsnt_clsc_usc FOREIGN KEY (user_consent_id) REFERENCES public.user_consent(id);


--
-- Name: user_consent fk_grntcsnt_user; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_consent
    ADD CONSTRAINT fk_grntcsnt_user FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: group_attribute fk_group_attribute_group; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_attribute
    ADD CONSTRAINT fk_group_attribute_group FOREIGN KEY (group_id) REFERENCES public.keycloak_group(id);


--
-- Name: keycloak_group fk_group_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_group
    ADD CONSTRAINT fk_group_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: group_role_mapping fk_group_role_group; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_role_mapping
    ADD CONSTRAINT fk_group_role_group FOREIGN KEY (group_id) REFERENCES public.keycloak_group(id);


--
-- Name: group_role_mapping fk_group_role_role; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.group_role_mapping
    ADD CONSTRAINT fk_group_role_role FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: realm_default_roles fk_h4wpd7w4hsoolni3h0sw7btje; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_default_roles
    ADD CONSTRAINT fk_h4wpd7w4hsoolni3h0sw7btje FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: realm_enabled_event_types fk_h846o4h0w8epx5nwedrf5y69j; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_enabled_event_types
    ADD CONSTRAINT fk_h846o4h0w8epx5nwedrf5y69j FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: realm_events_listeners fk_h846o4h0w8epx5nxev9f5y69j; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_events_listeners
    ADD CONSTRAINT fk_h846o4h0w8epx5nxev9f5y69j FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: identity_provider_mapper fk_idpm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_mapper
    ADD CONSTRAINT fk_idpm_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: idp_mapper_config fk_idpmconfig; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.idp_mapper_config
    ADD CONSTRAINT fk_idpmconfig FOREIGN KEY (idp_mapper_id) REFERENCES public.identity_provider_mapper(id);


--
-- Name: keycloak_role fk_kjho5le2c0ral09fl8cm9wfw9; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.keycloak_role
    ADD CONSTRAINT fk_kjho5le2c0ral09fl8cm9wfw9 FOREIGN KEY (client) REFERENCES public.client(id);


--
-- Name: web_origins fk_lojpho213xcx4wnkog82ssrfy; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.web_origins
    ADD CONSTRAINT fk_lojpho213xcx4wnkog82ssrfy FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: client_default_roles fk_nuilts7klwqw2h8m2b5joytky; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_default_roles
    ADD CONSTRAINT fk_nuilts7klwqw2h8m2b5joytky FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: scope_mapping fk_ouse064plmlr732lxjcn1q5f1; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_mapping
    ADD CONSTRAINT fk_ouse064plmlr732lxjcn1q5f1 FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: scope_mapping fk_p3rh9grku11kqfrs4fltt7rnq; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.scope_mapping
    ADD CONSTRAINT fk_p3rh9grku11kqfrs4fltt7rnq FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: client fk_p56ctinxxb9gsk57fo49f9tac; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT fk_p56ctinxxb9gsk57fo49f9tac FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: protocol_mapper fk_pcm_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper
    ADD CONSTRAINT fk_pcm_realm FOREIGN KEY (client_id) REFERENCES public.client(id);


--
-- Name: credential fk_pfyr0glasqyl0dei3kl69r6v0; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.credential
    ADD CONSTRAINT fk_pfyr0glasqyl0dei3kl69r6v0 FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: protocol_mapper_config fk_pmconfig; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.protocol_mapper_config
    ADD CONSTRAINT fk_pmconfig FOREIGN KEY (protocol_mapper_id) REFERENCES public.protocol_mapper(id);


--
-- Name: default_client_scope fk_r_def_cli_scope_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.default_client_scope
    ADD CONSTRAINT fk_r_def_cli_scope_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: default_client_scope fk_r_def_cli_scope_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.default_client_scope
    ADD CONSTRAINT fk_r_def_cli_scope_scope FOREIGN KEY (scope_id) REFERENCES public.client_scope(id);


--
-- Name: client_scope fk_realm_cli_scope; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.client_scope
    ADD CONSTRAINT fk_realm_cli_scope FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: required_action_provider fk_req_act_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.required_action_provider
    ADD CONSTRAINT fk_req_act_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: resource_uris fk_resource_server_uris; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.resource_uris
    ADD CONSTRAINT fk_resource_server_uris FOREIGN KEY (resource_id) REFERENCES public.resource_server_resource(id);


--
-- Name: role_attribute fk_role_attribute_id; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.role_attribute
    ADD CONSTRAINT fk_role_attribute_id FOREIGN KEY (role_id) REFERENCES public.keycloak_role(id);


--
-- Name: realm_supported_locales fk_supported_locales_realm; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm_supported_locales
    ADD CONSTRAINT fk_supported_locales_realm FOREIGN KEY (realm_id) REFERENCES public.realm(id);


--
-- Name: user_federation_config fk_t13hpu1j94r2ebpekr39x5eu5; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_federation_config
    ADD CONSTRAINT fk_t13hpu1j94r2ebpekr39x5eu5 FOREIGN KEY (user_federation_provider_id) REFERENCES public.user_federation_provider(id);


--
-- Name: realm fk_traf444kk6qrkms7n56aiwq5y; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.realm
    ADD CONSTRAINT fk_traf444kk6qrkms7n56aiwq5y FOREIGN KEY (master_admin_client) REFERENCES public.client(id);


--
-- Name: user_group_membership fk_user_group_user; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.user_group_membership
    ADD CONSTRAINT fk_user_group_user FOREIGN KEY (user_id) REFERENCES public.user_entity(id);


--
-- Name: policy_config fkdc34197cf864c4e43; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.policy_config
    ADD CONSTRAINT fkdc34197cf864c4e43 FOREIGN KEY (policy_id) REFERENCES public.resource_server_policy(id);


--
-- Name: identity_provider_config fkdc4897cf864c4e43; Type: FK CONSTRAINT; Schema: public; Owner: keycloak
--

ALTER TABLE ONLY public.identity_provider_config
    ADD CONSTRAINT fkdc4897cf864c4e43 FOREIGN KEY (identity_provider_id) REFERENCES public.identity_provider(internal_id);


--
-- PostgreSQL database dump complete
--

