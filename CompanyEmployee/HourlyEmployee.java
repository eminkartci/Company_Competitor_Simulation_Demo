public class HourlyEmployee extends Employee{

    // Attributes
    private int hours;
    private double rate;

    // Constructor
    public HourlyEmployee(String name, String surname, int employeeID,int hour,double rate) {
        super(name, surname, employeeID);
        this.hours = hours;
        this.rate = rate;
    }

    @Override
    public double earnings() {
        // First 40 hours the same - Extra hours you have to pay %50 more
        if (hours < 40 ){
            return rate * hours;
        }else{
            return 40 * rate + (hours-40) * rate * 1.5;
        }
    }
    

    // New toString
    public String toString() {
        return super.toString() + "\n"
            + "Employee Type    : Hourly Employee"  + "\n"
            + "Hours Worked     : " + this.hours    + "\n"
            + "Hourly Wage      : " + this.rate ;
    }

    
}
