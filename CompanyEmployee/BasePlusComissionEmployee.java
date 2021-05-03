public class BasePlusComissionEmployee extends ComissionEmployee{

    // New Attributes
    private double baseSalary;

    public BasePlusComissionEmployee(String name, String surname, int employeeID, double comissionRate,
            double grossSales, double baseSalary) {
        super(name, surname, employeeID, comissionRate, grossSales);
        this.baseSalary = baseSalary;
    }

    // Override
    public double earnings(){
        return super.earnings() + baseSalary;
    }

    public String toString() {
        return super.toString() + "\n Base Salary   : " + this.baseSalary;
    }
    
}
