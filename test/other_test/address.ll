; ModuleID = "address.cpp"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

declare i32 @"scanf"(i8* %".1", ...) 

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
__main:
  %"a" = alloca i32
  store i32 0, i32* %"a"
  %".3" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_0", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"scanf"(i8* %".3", i32* %"a")
  %".5" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_1", i32 0, i32 0
  %".6" = load i32, i32* %"a"
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %".6")
  ret i32 0
}

@"__string_0" = internal global [3 x i8] c"%d\00"
@"__string_1" = internal global [4 x i8] c"%d\0a\00"