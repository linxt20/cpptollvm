; ModuleID = "printf.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

@"__string_0" = internal global [6 x i8] c"abcba\00"
define i32 @"main"() 
{
__main:
  %"b" = alloca i32
  store i32 1, i32* %"b"
  %".3" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".4" = load i32, i32* %"b"
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".4")
  %".6" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_2", i32 0, i32 0
  %".7" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_0", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".6", i8* %".7")
  ret i32 0
}

@"__string_1" = internal global [4 x i8] c"%d\0a\00"
@"__string_2" = internal global [4 x i8] c"%s\0a\00"