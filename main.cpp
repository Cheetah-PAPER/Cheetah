#include <iostream>
#include <python.h> //导入

int main()
{
	Py_Initialize();   //初始化


	PyRun_SimpleString("import networkx as nx");
	PyRun_SimpleString("from timeit import default_timer as timer");

    PyRun_SimpleString("updates = ['1 2', '1 3', '1 4', '1 5', '2 5', '2 8']\nG = nx.Graph()\nfusion_updates_list = fuse(updates)\nfusion_updates_list = fuse(updates)\nfor fu in fusion_updates_list:\n\x20 explore(fu, G)");


	Py_Finalize();    //释放python
}
