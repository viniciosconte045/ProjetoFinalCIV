class Funcionario
{
    private string nome = "";
    private double salario;

    public string Nome
    {
        get { return nome; }
        set
        {
            if (value != "")
            {
                nome = value;
            }
        }
    }

    public double Salario
    {
        get { return salario; }
        set
        {
            if (value > 0)
            {
                salario = value;
            }
        }
    }

    public Funcionario(string nome, double salario)
    {
        Nome = nome;
        Salario = salario;
    }

    public override string ToString()
    {
        return "Funcionario: " + Nome + " | Salário: R$ " + Salario;
    }
}