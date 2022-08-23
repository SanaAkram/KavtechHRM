create table django_migrations
(
    id      bigserial
        primary key,
    app     varchar(255)             not null,
    name    varchar(255)             not null,
    applied timestamp with time zone not null
);

alter table django_migrations
    owner to postgres;

create table account_user
(
    id         bigserial
        primary key,
    password   varchar(128)             not null,
    last_login timestamp with time zone,
    email      varchar(255)             not null
        unique,
    name       varchar(200)             not null,
    is_active  boolean                  not null,
    is_admin   boolean                  not null,
    created_at timestamp with time zone not null,
    updated_at timestamp with time zone not null
);

alter table account_user
    owner to postgres;

create index account_user_email_0bd7c421_like
    on account_user (email varchar_pattern_ops);

create table account_kavprof
(
    id            bigserial
        primary key,
    first_name    varchar(10)  not null,
    last_name     varchar(10)  not null,
    experience    text         not null,
    b_degree      text         not null,
    b_institute   text         not null,
    m_degree      text         not null,
    m_institute   text         not null,
    phd_degree    text         not null,
    phd_institute text         not null,
    sched_test    varchar(50)  not null,
    user_fk_id    bigint       not null
        constraint account_kavprof_user_id_key
            unique
        constraint account_kavprof_user_fk_id_7100a350_fk_account_user_id
            references account_user
            deferrable initially deferred,
    job_openings  varchar(500) not null
);

alter table account_kavprof
    owner to postgres;

create table quiz_category
(
    id   bigserial
        primary key,
    name varchar(255) not null
);

alter table quiz_category
    owner to postgres;

create table quiz_quizzes
(
    id           bigserial
        primary key,
    title        varchar(255)             not null,
    date_created timestamp with time zone not null,
    category_id  bigint                   not null
        constraint quiz_quizzes_category_id_1122f3a5_fk_quiz_category_id
            references quiz_category
            deferrable initially deferred
);

alter table quiz_quizzes
    owner to postgres;

create table quiz_question
(
    id               bigserial
        primary key,
    date_updated     timestamp with time zone not null,
    title            varchar(255)             not null,
    difficulty_level integer                  not null,
    opt_1            varchar(255)             not null,
    opt_2            varchar(255)             not null,
    opt_3            varchar(255)             not null,
    opt_4            varchar(255)             not null,
    score            integer                  not null,
    date_created     timestamp with time zone not null,
    is_active        boolean                  not null,
    quiz_id          bigint                   not null
        constraint quiz_question_quiz_id_b7429966_fk_quiz_quizzes_id
            references quiz_quizzes
            deferrable initially deferred,
    right_opt        varchar                  not null
);

alter table quiz_question
    owner to postgres;

create index quiz_question_quiz_id_b7429966
    on quiz_question (quiz_id);

create table quiz_usersubmittedanswer
(
    id          bigserial
        primary key,
    right_ans   varchar(255) not null,
    user_fk_id  bigint       not null
        constraint quiz_usersubmittedan_user_fk_id_d3875b43_fk_account_k
            references account_kavprof
            deferrable initially deferred,
    question_id bigint       not null
        constraint quiz_usersubmittedan_question_id_69c42809_fk_quiz_ques
            references quiz_question
            deferrable initially deferred
);

alter table quiz_usersubmittedanswer
    owner to postgres;

create index quiz_usersubmittedanswer_can_id_id_c66b95cf
    on quiz_usersubmittedanswer (user_fk_id);

create index quiz_usersubmittedanswer_question_id_69c42809
    on quiz_usersubmittedanswer (question_id);

create index quiz_quizzes_category_id_1122f3a5
    on quiz_quizzes (category_id);

create table django_content_type
(
    id        serial
        primary key,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    constraint django_content_type_app_label_model_76bd3d3b_uniq
        unique (app_label, model)
);

alter table django_content_type
    owner to postgres;

create table django_admin_log
(
    id              serial
        primary key,
    action_time     timestamp with time zone not null,
    object_id       text,
    object_repr     varchar(200)             not null,
    action_flag     smallint                 not null
        constraint django_admin_log_action_flag_check
            check (action_flag >= 0),
    change_message  text                     not null,
    content_type_id integer
        constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
            references django_content_type
            deferrable initially deferred,
    user_id         bigint                   not null
        constraint django_admin_log_user_id_c564eba6_fk_account_user_id
            references account_user
            deferrable initially deferred
);

alter table django_admin_log
    owner to postgres;

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

create table auth_permission
(
    id              serial
        primary key,
    name            varchar(255) not null,
    content_type_id integer      not null
        constraint auth_permission_content_type_id_2f476e4b_fk_django_co
            references django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    constraint auth_permission_content_type_id_codename_01ab375a_uniq
        unique (content_type_id, codename)
);

alter table auth_permission
    owner to postgres;

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create table auth_group
(
    id   serial
        primary key,
    name varchar(150) not null
        unique
);

alter table auth_group
    owner to postgres;

create index auth_group_name_a6ea08ec_like
    on auth_group (name varchar_pattern_ops);

create table auth_group_permissions
(
    id            bigserial
        primary key,
    group_id      integer not null
        constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
            references auth_group
            deferrable initially deferred,
    permission_id integer not null
        constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
            references auth_permission
            deferrable initially deferred,
    constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
        unique (group_id, permission_id)
);

alter table auth_group_permissions
    owner to postgres;

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create table django_session
(
    session_key  varchar(40)              not null
        primary key,
    session_data text                     not null,
    expire_date  timestamp with time zone not null
);

alter table django_session
    owner to postgres;

create index django_session_session_key_c0390e0f_like
    on django_session (session_key varchar_pattern_ops);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table token_blacklist_outstandingtoken
(
    id         bigserial
        primary key,
    token      text                     not null,
    created_at timestamp with time zone,
    expires_at timestamp with time zone not null,
    user_id    bigint
        constraint token_blacklist_outs_user_id_83bc629a_fk_account_u
            references account_user
            deferrable initially deferred,
    jti        varchar(255)             not null
        constraint token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq
            unique
);

alter table token_blacklist_outstandingtoken
    owner to postgres;

create table token_blacklist_blacklistedtoken
(
    id             bigserial
        primary key,
    blacklisted_at timestamp with time zone not null,
    token_id       bigint                   not null
        unique
        constraint token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk
            references token_blacklist_outstandingtoken
            deferrable initially deferred
);

alter table token_blacklist_blacklistedtoken
    owner to postgres;

create index token_blacklist_outstandingtoken_user_id_83bc629a
    on token_blacklist_outstandingtoken (user_id);

create index token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_like
    on token_blacklist_outstandingtoken (jti varchar_pattern_ops);


