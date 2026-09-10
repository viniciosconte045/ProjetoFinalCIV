class Produto
{
    private string nome = "";
    private double preco;

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

    public double Preco
    {
        get { return preco; }
        set
        {
            if (value >= 0)
            {
                preco = value;
            }
        }
    }

    public Produto(string nome, double preco)
    {
        Nome = nome;
        Preco = preco;
    }

    public override string ToString()
    {
        return "Produto: " + Nome + " | Preço: R$ " + Preco;
    }
}