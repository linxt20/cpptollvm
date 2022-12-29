int printf(char* a, ...);
int scanf(char* a, ...);

char final[100];
int judgezero;

int strlen(char* s){
    int i;
    for(i=0;s[i]!='\0';i=i+1);
    return i;
}

void Polish(char* str){
    char s1[100];
    int index_1=0;
    int len=strlen(str);
    int t=1;
    int i=0;
    while(i<len){
        if(str[i]=='['){
            index_1 = index_1+1;
            s1[index_1]='[';
            i=i+1;
        }
        else if(str[i]==']'){
            while(s1[index_1]!='['){
                final[t]=s1[index_1];
                t=t+1;
                index_1=index_1-1;
            }
            index_1=index_1-1;
            i=i+1;
        }
        else if(str[i]=='+'||str[i]=='-'){
            while(index_1!=0&&s1[index_1]!='['){
                final[t]=s1[index_1];
                t=t+1;
                index_1 = index_1-1;
            }
            index_1=index_1+1;
            s1[index_1]=str[i];
            i=i+1;
        }
        else if(str[i]=='*'||str[i]=='/'){
            while(s1[index_1]=='*'||s1[index_1]=='/'){
                final[t]=s1[index_1];
                t=t+1;
                index_1=index_1-1;
            }
            index_1=index_1+1;
            s1[index_1]=str[i];
            i=i+1;
        }
        else{
            while(str[i]<='9'&&str[i]>='0'){
                final[t]=str[i];
                t=t+1;
                i=i+1;
            }
            final[t]=' ';
            t=t+1;
        }
    }
    while(index_1!=0){
        final[t]=s1[index_1];
        t=t+1;
        index_1=index_1-1;
    }
}

int cal(char* po){
    int stack[100];
    int index=-1;
    int n_data=0;
    int i;
    for(i=0;i<100;i=i+1){
        if(po[i]<='9' && po[i]>='0'){
            n_data=n_data*10+(po[i]-'0');
        }
        else if(po[i]==' '){
            index = index+1;
            stack[index]=n_data;
            n_data=0;
        }
        else if(po[i]=='+'){
            stack[index-1]=stack[index-1]+stack[index];
            index=index-1;
        }
        else if(po[i]=='-'){
            stack[index-1]=stack[index-1]-stack[index];
            index=index-1;
        }
        else if(po[i]=='*'){
            stack[index-1]=stack[index-1]*stack[index];
            index=index-1;
        }
        else if(po[i]=='/'){
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
    if(c=='+'|| c=='-'||  c=='*'||  c=='/'){
        return 1;
    }
    else if(c<='9'&&c>='0'){
        return 0;
    }
    else if(c=='['){
        return 2;
    }
    else if(c==']'){
        return 3;
    }
    else return -1;
}

int main(){
    judgezero = 0;
    char strs[100];
    char stringone[100];
    scanf("%s",stringone);
    // scanf("%s",&strs);
    int len=strlen(stringone);
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

    Polish(strs);

    int num=cal(final);
    if(judgezero==1){
        return 0;
    }
    printf("%d\n",num);
    return 0;
}