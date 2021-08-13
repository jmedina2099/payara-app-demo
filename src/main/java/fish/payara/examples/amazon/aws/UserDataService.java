package fish.payara.examples.amazon.aws;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;

@ApplicationScoped
public class UserDataService {

    private Map<Integer, UserData> dataSet = new HashMap<>();

    @Inject
    private InstanceInfoService infoService;

    @Inject
    private CounterService counterService;

    public Optional<UserData> retrieve(Integer id) {
        return Optional.ofNullable(dataSet.get(id));
    }

    public UserData store(UserData userData) {
        Integer id = counterService.getNextValue();
        dataSet.putIfAbsent(id, new UserData(id, userData, infoService.getName()));
        return dataSet.get(id);
    }

    public List<UserData> listAll() {
        List<UserData> result = new ArrayList<>();
        dataSet.values().forEach(result::add);
        return result;
    }
}
