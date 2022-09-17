; ModuleID = 'main.adept'
source_filename = "main.adept"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-darwin21.4.0"

@__stdinp = external global { [32 x i64] }*
@__stderrp = external global { [32 x i64] }*
@__stdoutp = external global { [32 x i64] }*
@g2 = internal global { i64, i8*, i1, i64 }** null
@g2.1 = internal global i8** null
@g2.2 = internal global i64 0
@g2.3 = internal global i64 0
@S0 = internal constant [4 x i8] c"%c\0A\00"

declare i32 @system(i8* %0)

declare void @exit(i32 %0)

declare void @abort()

declare void @atexit(void ()* %0)

declare i8* @calloc(i64 %0, i64 %1)

declare void @free(i8* %0)

declare i8* @malloc(i64 %0)

declare i8* @realloc(i8* %0, i64 %1)

declare double @atof(i8* %0)

declare i32 @atoi(i8* %0)

declare i64 @atol(i8* %0)

declare double @strtod(i8* %0, i8** %1)

declare i64 @strtol(i8* %0, i8** %1, i32 %2)

declare i64 @strtoul(i8* %0, i8** %1, i32 %2)

declare i32 @abs(i32 %0)

declare i64 @labs(i64 %0)

declare i8* @getenv(i8* %0)

declare void @qsort(i8* %0, i64 %1, i64 %2, i8* %3)

declare i8* @bsearch(i8* %0, i8* %1, i64 %2, i64 %3, i32 (i8*, i8*)* %4)

declare i32 @rand()

declare void @srand(i32 %0)

declare i32 @remove(i8* %0)

declare i32 @rename(i8* %0, i8* %1)

declare { [32 x i64] }* @tmpfile()

declare i32 @fclose({ [32 x i64] }* %0)

declare i32 @fflush({ [32 x i64] }* %0)

declare { [32 x i64] }* @fopen(i8* %0, i8* %1)

declare { [32 x i64] }* @freopen(i8* %0, i8* %1, { [32 x i64] }* %2)

declare void @setbuf({ [32 x i64] }* %0, i8* %1)

declare i32 @setvbuf({ [32 x i64] }* %0, i8* %1, i32 %2, i64 %3)

declare i32 @fgetc({ [32 x i64] }* %0)

declare i8* @fgets(i8* %0, i32 %1, { [32 x i64] }* %2)

declare i32 @fputc(i32 %0, { [32 x i64] }* %1)

declare i32 @fputs(i8* %0, { [32 x i64] }* %1)

declare i32 @getc({ [32 x i64] }* %0)

declare i32 @putc(i32 %0, { [32 x i64] }* %1)

declare i32 @putchar(i32 %0)

declare i32 @getchar()

declare i32 @ungetc(i32 %0, { [32 x i64] }* %1)

declare i32 @puts(i8* %0)

declare i8* @gets(i8* %0)

declare i32 @fread(i8* %0, i64 %1, i64 %2, { [32 x i64] }* %3)

declare i32 @fwrite(i8* %0, i64 %1, i64 %2, { [32 x i64] }* %3)

declare i32 @fgetpos({ [32 x i64] }* %0, i64* %1)

declare i32 @fseek({ [32 x i64] }* %0, i32 %1, i32 %2)

declare i32 @fsetpos({ [32 x i64] }* %0, i64* %1)

declare i32 @ftell({ [32 x i64] }* %0)

declare void @rewind({ [32 x i64] }* %0)

declare void @clearerr({ [32 x i64] }* %0)

declare i32 @feof({ [32 x i64] }* %0)

declare i32 @ferror({ [32 x i64] }* %0)

declare void @perror(i8* %0)

declare i32 @printf(i8* %0, ...)

declare i32 @fprintf({ [32 x i64] }* %0, i8* %1, ...)

declare i32 @sprintf(i8* %0, i8* %1, ...)

declare i32 @snprintf(i8* %0, i64 %1, i8* %2, ...)

declare i32 @scanf(i8* %0, ...)

declare i32 @fscanf({ [32 x i64] }* %0, i8* %1, ...)

declare i32 @sscanf(i8* %0, i8* %1, ...)

declare i32 @vprintf(i8* %0, { i8* } %1)

declare i32 @vfprintf({ [32 x i64] }* %0, i8* %1, { i8* } %2)

declare i32 @vsprintf(i8* %0, i8* %1, { i8* } %2)

declare i32 @vsnprintf(i8* %0, i64 %1, i8* %2, { i8* } %3)

declare i32 @vscanf(i8* %0, { i8* } %1)

declare i32 @vfscanf({ [32 x i64] }* %0, i8* %1, { i8* } %2)

declare i32 @vsscanf(i8* %0, i8* %1, { i8* } %2)

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
  call void @____adeinitsvars()
  ret i32 0

17:                                               ; preds = %13, %1
  %18 = load i64, i64* %3, align 8
  %19 = icmp ult i64 %18, 9
  br i1 %19, label %5, label %16

20:                                               ; preds = %0
  br label %1
}

define private void @____adeinitsvars() {
  ret void
}

attributes #0 = { nounwind }