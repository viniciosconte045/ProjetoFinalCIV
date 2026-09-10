class Turma
{
    public List<Aluno> Alunos = new List<Aluno>();

    public void ListarAlunos()
    {
        foreach (var aluno in Alunos)
        {
            aluno.ExibirInfo();
            Console.WriteLine($"Situaçao: {aluno.ObterSituaçao()}");
            Console.WriteLine();
        }
    }
    public float CalcularMedia()
    {
        float totalNotas = 0;
        foreach (Alunos aluno in Alunos)
        {
            totalNotas += aluno.Nota;
        }
        return totalNotas / Alunos.Count;
    }
}
