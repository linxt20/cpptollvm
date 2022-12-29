; ModuleID = "str.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

@"__string_0" = internal global [14 x i8] c"hello, world!\00"
define i32 @"main"() 
{
__main:
  %".2" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_1", i32 0, i32 0
  %".3" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", i8* %".3")
  %".5" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 1
  %".6" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 0
  %".7" = load i8, i8* %".6"
  store i8 %".7", i8* %".5"
  %".9" = load i8, i8* %".5"
  %".10" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".11" = getelementptr inbounds [14 x i8], [14 x i8]* @"__string_0", i32 0, i32 0
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".10", i8* %".11")
  ret i32 0
}

@"__string_1" = internal global [3 x i8] c"%s\00"
@"__string_2" = internal global [3 x i8] c"%s\00"