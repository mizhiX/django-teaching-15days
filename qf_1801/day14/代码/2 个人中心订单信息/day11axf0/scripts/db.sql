

create table axf_users_ticket(
    id int auto_increment primary key,
    user_id int not null,
    ticket varchar(256) not null,
    out_time TIMESTAMP,
    foreign key(user_id) references axf_users(id)
);