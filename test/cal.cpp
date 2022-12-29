int printf(char* a, ...);
int scanf(char* a, ...);

char final[100];
char strs[100];
char stringone[100];
int judgezero;

int Polish(){ 
    char s1[100];
    int index_1=0;
    int len;
    for(len=0;strs[len]!=0;len=len+1);
    int t=0; // 这个原来是 t=1;
    int i=0;
    while(i<len){
        if(strs[i]==91){
            index_1 = index_1+1;
            s1[index_1]=91;
            i=i+1;
        }
        else if(strs[i]==93){
            while(s1[index_1]!=91){
                final[t]=s1[index_1];
                t=t+1;
                index_1=index_1-1;
            }
            index_1=index_1-1;
            i=i+1;
        }
        else if(strs[i]==43||strs[i]==45){
            while(index_1!=0&&s1[index_1]!=91){
                final[t]=s1[index_1];
                t=t+1;
                index_1 = index_1-1;
            }
            index_1=index_1+1;
            s1[index_1]=strs[i];
            i=i+1;
        }
        else if(strs[i]==42||strs[i]==47){
            while(s1[index_1]==42||s1[index_1]==47){
                final[t]=s1[index_1];
                t=t+1;
                index_1=index_1-1;
            }
            index_1=index_1+1;
            s1[index_1]=strs[i];
            i=i+1;
        }
        else{
            while(strs[i]<=57&&strs[i]>=48){
                final[t]=strs[i];
                t=t+1;
                i=i+1;
            }
            final[t]=32;
            t=t+1;
        }
    }
    while(index_1!=0){
        final[t]=s1[index_1];
        t=t+1;
        index_1=index_1-1;
    }
    return 0;
}

int cal(){
    int stack[100];
    int index=-1;
    int n_data=0;
    int i;
    for(i=0;i<100;i=i+1){
        if(final[i]<=57 && final[i]>=48){
            n_data=n_data*10+(final[i]-48);
        }
        else if(final[i]==32){
            index = index+1;
            stack[index]=n_data;
            n_data=0;
        }
        else if(final[i]==43){
            stack[index-1]=stack[index-1]+stack[index];
            index=index-1;
        }
        else if(final[i]==45){
            stack[index-1]=stack[index-1]-stack[index];
            index=index-1;
        }
        else if(final[i]==42){
            stack[index-1]=stack[index-1]*stack[index];
            index=index-1;
        }
        else if(final[i]==47){
            if(stack[index]!=0){
                stack[index-1]=stack[index-1]/stack[index];
                index=index-1;
            }
            else{
                printf("error:divisor is zero\n");
                judgezero = 1;
                return 0;
            }
        }
    }
    return stack[index];
}
int judge(char c){
    int typejudge = -1;
    if(c==43|| c==45||  c==42||  c==47){
        typejudge = 1;
    }
    else{
        if(c<=57&&c>=48){
            typejudge = 0;
        }
        else{
            if(c==91){
                typejudge =2;
            }
            else{
                if(c==93){
                    typejudge =3;
                }
            } 
        }             
    }
    return typejudge;
}

int main(){
    judgezero = 0;
    scanf("%s",stringone);
    // scanf("%s",&strs);
    int len;
    for(len=0;stringone[len]!=0;len++);
    int left=0;
    int pst = -2;
    int i;
    for(i=0;i<len;i=i+1){
        int jud=judge(stringone[i]);
        if(jud>=0){
            if(i!=0){
                if(pst==1&&jud==1){
                    printf("error:input 2 continuous ops\n");
                    return 0;
                }
                else if(pst==2&&jud!=0){
                    printf("error:input \'[\' without following number\n");
                    return 0;
                }
                else if(pst==3&&jud==0){
                    printf("error:input \']\' with following number\n");
                    return 0;
                }
                else if(pst==0&&jud==2){
                    printf("error:input number with following \'[\'\n");
                    return 0;
                }
                else if(pst!=0&&jud==3){
                    printf("error:before \']\' there\'s no number\n");
                    return 0;
                }
                pst=jud;
            }
            else{
                if(jud==1||jud==3){
                    printf("error:expression cannot start with an op or \']\'\n");
                    return 0;
                }
                pst=jud;
            }
            if(jud==2){
                left=left+1;
            }
            else if(jud==3){
                left=left-1;
            }
            strs[i]=stringone[i];
            if(left<0){
                printf("error:unmatched []\n");
                return 0;
            }
        }
        else{
            printf("error:input unaccepted\n");
            return 0;
        }
    }
    if(left!=0){
        printf("error:unmatched []\n");
        return 0;
    }

    Polish();

    int num=cal();
    if(judgezero==1){
        return 0;
    }
    printf("%s\n",final);
    printf("%d\n",num);
    return 0;
}