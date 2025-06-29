namespace Problems
{
    public class Problem_1 : IProblem
    {
        public void Run()
        {
            int sum = 0;

            for(int i=1; i<1000; i++){
                if(i % 3 == 0 || i % 5 == 0){
                    // Console.WriteLine(i);
                    sum = sum + i;
                }
            }

            Console.WriteLine(sum);
        }
    }
}