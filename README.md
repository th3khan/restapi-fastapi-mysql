# Rest API with Fast API and MySQL

Simple Rest API with Fast Api and MySQL

# Get All Users
[Method] GET<br/>
@Return List[User]<br/>
@Path /users

# Create user
[Method] POST<br/>
@Params user: User<br/>
@Return ResponseBase[User]<br/>
@Path /user

# Get User
[Method] GET<br/>
@Params id: int<br/>
@Return User<br/>
@Path /user/{id}

# Update User
[Method] PUT<br/>
@Params id: int, user: User<br/>
@Return ResponseBase[User]<br/>
@Path /user/{id}

# Delete User
[Method] DELETE<br/>
@Params id: int<br/>
@Return ResponseBase[None]<br/>
@Path /user/{id}