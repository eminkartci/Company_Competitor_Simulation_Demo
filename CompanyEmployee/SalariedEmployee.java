public class SalariedEmployee extends Employee{

    // New Attributes
    private double monthlySalary;

    public SalariedEmployee(String name, String surname, int employeeID, double monthlySalary) {
        // Call super constructor
        super(name, surname, employeeID);
        this.monthlySalary = monthlySalary;
    }

    // If you want to make this class concrete override it
    @Override
    public double earnings() {
        return monthlySalary;
    }

    // Override to String method
    public String toString(){
            // Call super class get same info
        return super.toString() + "\n"
            // Additional ones
              + "Employee Type  : Monthly Salary" 
              + "Monthly Salary : " + this.monthlySalary;
    }
    
}
