
public class ComissionEmployee extends Employee{

    // New Attributes
    private double comissionRate;
    private double grossSales;

    public ComissionEmployee(String name, String surname, int employeeID,double comissionRate , double grossSales) {
        super(name, surname, employeeID);
        this.comissionRate  = comissionRate;
        this.grossSales     = grossSales;
    }

    @Override
    public double earnings() {
        return comissionRate * grossSales;
    }

    // New toString
    public String toString() {
        return super.toString() + "\n"
            + "Employee Type    : Comission Employee"  + "\n"
            + "Comission Rate   : " + this.comissionRate 
            + "Gross Sales      : " + this.grossSales;
    }

}