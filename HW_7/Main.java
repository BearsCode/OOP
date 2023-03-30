package HW_7;

import HW_7.logger.Decorator;
// import HW_7.logger.LoggerAble;
import HW_7.logger.LoggerTerminal;
import HW_7.controllers.UserController;
import HW_7.model.FileOperation;
import HW_7.model.FileOperationImpl;
import HW_7.model.Repository;
import HW_7.model.RepositoryFile;
import HW_7.utils.Validate;
import HW_7.views.ViewUser;

public class Main {
    public static void main(String[] args) {
        FileOperation fileOperation = new FileOperationImpl( ""C:\Users\Эмиль\Desktop\GitHub\OOP\HW_7\users.txt"");
        // Repository repository = new RepositoryFile(fileOperation);
        Repository repository = new Decorator(new RepositoryFile(fileOperation), new LoggerTerminal());
        Validate validate = new Validate();
        UserController controller = new UserController(repository, validate);
        ViewUser view = new ViewUser(controller, validate);

        view.run();
    }
}
