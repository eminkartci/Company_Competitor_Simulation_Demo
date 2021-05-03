
public abstract class Employee{

    // Attributes
    private String name,surname;
    private int employeeID;  

    // constructor
    public Employee(String name,String surname,int employeeID){
        this.name = name;
        this.surname = surname;
        this.employeeID = employeeID;
    }

    // GETTER SETTERS

    public String getName(){
        return this.name;
    }

    public String getSurname(){
        return this.surname;
    }

    public int getEmployeeID(){
        return this.employeeID;
    }
    public void setName(String name){
        this.name = name;
    }

    public void setSurame(String surname){
        this.surname = surname;
    }

    // To string
    public String toString(){
        return "\n--- Employee "    + this.employeeID +" ---\n" 
                +"| Name        : " + this.name       +"\n" 
                +"| Surname     : " + this.surname;
    }

    // So that every employee subclass need yo overwrite this method
    public abstract double earnings();
    
}