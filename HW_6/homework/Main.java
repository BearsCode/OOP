package HW_6.homework;

public class Main{
	public static void main(String[] args){
		User user = new User("Bob");
		Persister pers = new Persister(user);
		Report report = new Report();
		report.report(user);
		pers.save();
	}
}