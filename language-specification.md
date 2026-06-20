# ai-kaizen-lang (aikai) Spec v1.0

## 1. 基本方針

- 構文は単純・一意
- 糖衣構文なし
- 同一処理は同一記法
- 暗黙動作を禁止
- LLMが誤解しないことを最優先

---

## 2. 命名規則

- 予約語：大文字
- 識別子：小文字スネークケース
- コメント：行頭 `#` のみ

---

## 3. 文

- 1行 = 1文
- 途中改行禁止

---

## 4. 型

### 基本型
- INT
- STRING
- BOOL

### 複合型
- ARRAY ! TYPE
- STRUCT name ... END STRUCT

### 特殊型
- REF TYPE
- TASK TYPE

---

## 5. 型システム

- 完全静的型
- 完全明示型
- 名義的型システム（STRUCTは名前で識別）
- 型の完全一致のみ許可
- 暗黙型変換は禁止

---

## 6. 値と式

### value
- リテラル
- 変数
- 関数呼び出し結果
- STRUCT初期化

### expr
- value OP value

### 制約
- exprは1演算のみ
- ネスト禁止
- valueはexprではない
- 複雑な計算はLETで分解

---

## 7. 演算子

- 算術: + - * / %
- 比較: == != < <= > >=
- 論理: && ||
- ビット: & | ^ << >>

---

## 8. 変数
LET TYPE name = value_or_expr VAR TYPE name = value_or_expr

- 型必須
- 初期化必須
- LETは不変
- VARは再代入可能

---

## 9. 代入
name = value_or_expr

- VARのみ可能

---

## 10. 制御

### IF
IF condition statements ELSE statements END IF

- conditionはBOOLのみ

---

### FOR
FOR array AS item statements END FOR

- ARRAYのみ対象

---

## 11. 関数

### 定義
TYPE FUNC name PARAM TYPE param ... statements RETURN value_or_expr END FUNC

### 呼び出し
LET TYPE v = func arg1 arg2

### 制約

- 引数はvalueのみ（expr禁止）
- 戻り値は1つのみ

---

## 12. ERROR処理

### ERROR関数
TYPE FUNC name ... ERROR

### raise
std.error.raise "ERROR_CODE"

### ERRORブロック
FUNC ... statements ERROR err handler END FUNC

### ルール

- raiseは必ず伝播
- 同一関数内では捕捉不可
- ERRORは下位関数のみ捕捉
- 非ERROR関数がERROR関数を呼ぶ場合はERRORブロック必須

### 状態

- ERRORは状態を巻き戻さない

---

## 13. リソース管理

- スコープ終了時に自動解放
- ERROR時も解放
- 解放順はLIFO

---

## 14. メモリモデル

- すべて値渡し
- REFで明示参照
- 副作用はREF経由のみ

### REF制約

- REFはVARのみ対象
- REF引数にはVARのみ渡せる

---

## 15. STRUCT

### 定義
STRUCT name TYPE field END STRUCT

### 初期化
LET name v = { value1, value2 }

- 順序一致必須
- 省略不可

### 特性

- 不変（フィールド変更不可）

---

## 16. ARRAY

- 要素は同一型のみ
- 型は明示

---

## 17. 並列

### spawn
LET TASK TYPE t = std.task.spawn func arg1 arg2

### join
LET TYPE v = std.task.join t

---

### 並列ルール

- spawnはERROR関数も許可
- 引数はspawn時に評価・コピー
- ERRORはjoin時に発生
- 未joinはスコープ終了時に暗黙join
- 暗黙joinでもERRORはraise
- ERROR発生後は以降処理されない
- 並列関数にREF引数は禁止
- 副作用（IO）は許可
- 副作用順序は未定義

---

## 18. キャンセル
std.task.cancel t

- join時に raise "CANCELLED"
- 観測点でのみ発生

---

## 19. モジュール
IMPORT full.path.module AS alias

- フルパス必須
- 循環参照禁止

---

## 20. 禁止事項

- 糖衣構文
- 暗黙型変換
- exprネスト
- 複合式
- 関数引数へのexpr
- 不明確な共有状態
- 並列でのREF使用

---

## 21. 構文（EBNF）

### expr
expr = value operator value ;

### value
value = literal | identifier | func_call | struct_literal ;

### func_call
identifier value...

---

## 22. 実行モデル

- ASTベース実行
- ERRORは例外的制御
- 並列はjoin時に同期

---

## 23. コンパイラ構成

1. Lexer
2. Parser
3. AST生成
4. 型チェック
5. ERROR検証
6. 並列制約検証
7. 実行

---

## 24. 設計の本質

- 式を1段に制限
- 副作用をREFに限定
- ERRORを単一経路に統一
- 並列を安全側に制限

---

## 25. 特徴

- 曖昧性ゼロ
- LLM誤解耐性最大
- 実装容易
- 並列安全
