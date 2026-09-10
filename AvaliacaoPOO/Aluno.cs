class Aluno
{
    private string nome = "";
    private int idade;

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

    public int Idade
    {
        get { return idade; }
        set
        {
            if (value > 0)
            {
                idade = value;
            }
        }
    }

    public Aluno(string nome, int idade)
    {
        Nome = nome;
        Idade = idade;
    }

    public override string ToString()
    {
        return "Nome: " + Nome + " | Idade: " + Idade;
    }
}