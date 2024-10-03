#include <stdio.h>


int main(){

    int vaqt = 24;
    int rivojlanish = 1;
    int maqsad ;

    printf("Maqsadingiz bormi : \n ha = 1\n yo'q 0\n : ");
    scanf("%d",&maqsad);

    while (vaqt>0)
    {
        if (maqsad>0)
        {
            rivojlanish+=rivojlanish;

            printf("Rivojlanish = : %d \n",rivojlanish);
            
            vaqt--;
        }
        else{
            vaqt-=24;
        }
    }
    
}