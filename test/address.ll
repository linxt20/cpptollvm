; ModuleID = "address.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"scanf"(i8* %".1", ...) 

declare i32 @"printf"(i8* %".1", ...) 

@"a" = internal global i32 0
define i32 @"main"() 
{
__main:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"scanf"(i8* %".2", i32* @"a")
  %".4" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".5" = load i32, i32* @"a"
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".5")
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [4 x i8] c"%d\0a\00"