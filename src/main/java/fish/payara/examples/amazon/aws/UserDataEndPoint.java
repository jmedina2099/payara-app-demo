package fish.payara.examples.amazon.aws;


import java.util.List;

import javax.inject.Inject;
import javax.inject.Singleton;
import javax.validation.Valid;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.NotFoundException;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriBuilder;
import javax.ws.rs.core.UriInfo;

@Path("/data")
@Singleton
public class UserDataEndPoint {
	
    @Inject
    private UserDataService userDataService;

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createUser( @Valid UserData data, @Context UriInfo uriInfo) {
        UserData newUser = userDataService.store(data);
        return Response.created(UriBuilder.fromPath(uriInfo.getPath()).path("{id}").build(newUser.getId())).build();
    }

    @GET
    @Path("/{id}")
    public Response getUser(@PathParam("id") Integer id) {
        return userDataService.retrieve(id).map(Response::ok).map(Response.ResponseBuilder::build)
                .orElseThrow(NotFoundException::new);
    }

    @GET
    @Path("/all")
    public List<UserData> getAllUsers() {
        return userDataService.listAll();
    }
}

