package fish.payara.examples.amazon.aws;

import java.io.Serializable;

import javax.json.bind.annotation.JsonbCreator;
import javax.json.bind.annotation.JsonbProperty;
import javax.validation.constraints.NotNull;

import org.hibernate.validator.constraints.NotEmpty;

public class UserData implements Serializable {

    private static final long serialVersionUID = 1024713371902278434L;

    private Integer id;

    @NotNull
    @NotEmpty
    private String name;

    @NotNull
    @NotEmpty
    private String organization;

    private String createdOn;
    
    @JsonbCreator
    public UserData(@JsonbProperty("name") String name, @JsonbProperty("organization") String organization) {
        this.name = name;
        this.organization = organization;
    }

    public UserData(Integer id, UserData data, String createdOn) {
        this.id = id;
        this.name = data.name;
        this.organization = data.organization;
        this.createdOn = createdOn;
    }

    @JsonbProperty("id")
    public Integer getId() {
        return id;
    }

    @JsonbProperty("name")
    public String getName() {
        return name;
    }

    @JsonbProperty("organization")
    public String getOrganization() {
        return organization;
    }

    @JsonbProperty("createdOnInstance")
    public String getCreatedOn() {
        return createdOn;
    }
    
    @Override
    public String toString() {
    	return name + " - " + organization;
    }
}

