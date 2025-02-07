# ft_package

A sample test package.

このパッケージは、リスト内の指定した要素の出現回数を返す関数 `count_in_list` を提供します。

## 使用例
 python -m build

 pip install ./dist/ft_package-0.0.1.tar.gz


pip install ./dist/ft_package-0.0.1-py3-none-any.whl

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 出力: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 出力: 0
