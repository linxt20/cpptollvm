# cpptollvm
编译大作业——C++转为LLVM（中间表示）的编译器

使用方法：

1. 使用Antlr4把语法文件转化为源文件：

	1. 安装较新版本的Java JDK以及Antlr4（我们使用的是4.11.1）。
	2. 将下载的Antlr4对应的jar文件设置到Java class路径中，并且创建两个bat文件放入环境变量。
	3. 第一个是`antlr4.bat`，内容为`java org.antlr.v4.Tool %*`
	4. 第二个是`grun.bat`，内容为`java org.antlr.v4.gui.TestRig %*`（用于展示语法树，用于语法分析，对于编译来说不必要）
	5. 在根目录下运行`make antlr`，即利用`grammar`下的语法文件，生成`src`文件夹下的源文件。
	6. 请注意，如果您不需要修改语法文件或将项目迁移到其他语言，则可以直接利用`src`下已经转化好的源文件，跳过此步。

2. 运行编译器：

	1. 安装Python（我们使用的是Python 3.9）。
	2. 安装`requirements.txt`中的依赖库，方法为`pip install -r requirements.txt`。
	3. 进行编译，方法是`python main.py <inputfilename>`，这将在输入的C++文件旁创建一个同名的`.ll`文件，即为输出的LLVM文件。

3. 批量测试与清理输出：

	1. 如果您需要批量测试，可以在根目录下运行`make test`，这将遍历`test`和`test\other_test`文件夹下的所有`.cpp`文件完成编译。
	2. 如果您需要清理上一步产生的`.ll`文件输出，您可以在根目录下运行`make clean`，这将清理`test`和`test\other_test`文件夹下的所有`.ll`文件。

4. 使用LLVM运行编译结果：

	1. 我们的编译器默认输出在x86_64的Linux系统下运行的LLVM文件。如果需要检测编译器输出的`.ll`文件的正确性，您可以在Linux下配置环境（我们使用的是Ubuntu 20.04）：

		```bash
		sudo apt install clang-format clang-tidy clang-tools clang clangd
		sudo apt install lld lldb llvm-dev llvm-runtime llvm python-clang
		sudo apt install libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-11-dev libllvm-ocaml-dev libomp-dev libomp5
		```

	2. 执行LLVM程序：`lli <filename.ll>`

	3. 编译为汇编代码：`llc <filename.ll>`

