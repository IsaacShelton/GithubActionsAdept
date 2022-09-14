source_filename = ""
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-darwin21.4.0"

@S0 = internal constant [4 x i8] c"%c\0A\00"

declare i32 @printf(i8* %0, ...)

; Function Attrs: nounwind
define private [9 x i64] @a41() #0 {
  %1 = alloca [9 x i64], align 8
  %2 = alloca i64, align 8
  store [9 x i64] zeroinitializer, [9 x i64]* %1, align 8
  store i64 0, i64* %2, align 8
  br label %13

3:                                                ; preds = %13
  %4 = load i64, i64* %2, align 8
  %5 = load i64, i64* %2, align 8
  %6 = bitcast [9 x i64]* %1 to i64*
  %7 = getelementptr i64, i64* %6, i64 %5
  store i64 %4, i64* %7, align 8
  br label %8

8:                                                ; preds = %3
  %9 = load i64, i64* %2, align 8
  %10 = add i64 %9, 1
  store i64 %10, i64* %2, align 8
  br label %13

11:                                               ; preds = %13
  %12 = load [9 x i64], [9 x i64]* %1, align 8
  ret [9 x i64] %12

13:                                               ; preds = %8, %0
  %14 = load i64, i64* %2, align 8
  %15 = icmp ult i64 %14, 9
  br i1 %15, label %3, label %11
}

; Function Attrs: nounwind
define i32 @main() #0 {
  br label %20

1:                                                ; preds = %20
  %2 = alloca [9 x i64], align 8
  %3 = alloca i64, align 8
  %4 = call [9 x i64] @a41()
  store [9 x i64] %4, [9 x i64]* %2, align 8
  store i64 0, i64* %3, align 8
  br label %17

5:                                                ; preds = %17
  %6 = load i64, i64* %3, align 8
  %7 = bitcast [9 x i64]* %2 to i64*
  %8 = getelementptr i64, i64* %7, i64 %6
  %9 = load i64, i64* %8, align 8
  %10 = trunc i64 %9 to i8
  %11 = add i8 65, %10
  %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @S0, i32 0, i32 0), i8 %11)
  br label %13

13:                                               ; preds = %5
  %14 = load i64, i64* %3, align 8
  %15 = add i64 %14, 1
  store i64 %15, i64* %3, align 8
  br label %17

16:                                               ; preds = %17
  ret i32 0

17:                                               ; preds = %13, %1
  %18 = load i64, i64* %3, align 8
  %19 = icmp ult i64 %18, 9
  br i1 %19, label %5, label %16

20:                                               ; preds = %0
  br label %1
}

attributes #0 = { nounwind }
