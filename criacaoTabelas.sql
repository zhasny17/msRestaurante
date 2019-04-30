
CREATE DATABASE "restaurante";


CREATE DOMAIN public.nome         text;
CREATE DOMAIN public.senha        character varying(10);
CREATE DOMAIN public.nota         numeric(2,2);

CREATE TABLE cdusuario(
    id                       serial                        NOT NULL           ,   
    nome                     nome                          NOT NULL           ,    
    email                    text                          NOT NULL           ,   
    senha                    senha                         NOT NULL           ,  
    qualificacao             text                                             ,   
    tipo                     text                          NOT NULL           ,    
    CONSTRAINT cdusuario_pkey PRIMARY KEY (id),
    CONSTRAINT uk_cdusuario_1 UNIQUE (email),
    CONSTRAINT uk_cdusuario_2 UNIQUE (nome));


CREATE TABLE cdreceita(
    id                          serial                  NOT NULL           ,   
    nome                        nome                    NOT NULL           ,   
    tipo_receita                text                    NOT NULL           ,  
    nota                        nota                    Default NULL       ,      
    id_usuario                  Integer                 NOT NULL           ,   
    ultimaatuali                date                                       ,   
    preparo                     text                                       ,
    CONSTRAINT cdraceita_pkey PRIMARY KEY (id) ,
    CONSTRAINT fk_cdraceita_1 FOREIGN KEY (id_usuario)
        REFERENCES public.cdusuario (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);



    

CREATE TABLE cdingrediente(
    id                        serial                  NOT NULL           ,   
    nome                      nome                    NOT NULL           ,   
    quantidade                Integer                 NOT NULL           ,    
    id_receita                Integer                 NOT NULL           ,  
    CONSTRAINT cdingrediente_pkey PRIMARY KEY (id),
    CONSTRAINT fk_cdingrediente_1 FOREIGN KEY (id_receita)
        REFERENCES public.cdreceita (id) MATCH SIMPLE ON UPDATE CASCADE ON DELETE CASCADE);