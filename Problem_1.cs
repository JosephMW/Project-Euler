using System;

namespace Project_Euler
{
    class Problem_1
    {
        static void Main(string[] args)
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

// public class Problem_1{

//     public static void main(){
//         int sum = 0

//         for(int i=1; i<1000; i++){
//             if(i % 3 == 0 || i % 5 == 0){
//                 print(i)
//                 sum = sum + i
//             }
//         }

//         print(sum)
//     }     

// }
