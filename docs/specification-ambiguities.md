# LLM K Language Implementation - Specification Ambiguities

実装を進める上で、現在の `language-specification` では定義が曖昧、または欠落しているため、定義や方針の決定が必要な事項です。

## 1. 算術演算とカッコの優先順位
*   **現状:** `2.6 Parentheses` で、カッコが「演算の優先順位制御」のために使用できないと定義されている。
*   **不明点:** 
    *   カッコが使えない場合、`a + b * c` のような式の評価順序はどのように定義されるのか。
    *   計算順序が不明確だと「決定論的」ではなくなる。数学的な標準優先順位に従うのか、左結合のみを許可するのかを定義する必要がある。

*   **回答:**
    *   Expressions shall contain at most one operator. と記載しております。記載が揺れていたため、次の表現に統一しました。An expression shall contain at most one operator.

    10章の文法にも下記追記しました。
    binary_expression =
    operand binary_operator operand ;

## 2. 算術演算子の仕様
*   **現状:** `11. Expressions and Operators` で定義されるはずだが、具体的な演算子（`+`, `-`, `*`, `/`, `%` など）と、それがどの型に対して有効なのか、オーバーフロー時の挙動が不明。
*   **不明点:**
    *   整数型同士の除算は切り捨てか、浮動小数点になるのか。
    *   `INT`型などの数値型の境界値やオーバーフロー時のハンドリングはどうするのか（エラーにするか、ラップアラウンドか）。

*   **回答:**
    *   ✅T.B.D. 追記中。

## 3. 型のキャストと変換
*   **現状:** `04. Built-in Type System` や `13. TYPE System` に、明示的な型変換（キャスト）についての言及がない。
*   **不明点:**
    *   型同士の互換性や、型を明示的に変換する構文が必要か。AIがコードを生成する際、型不一致エラーが発生しやすいため、キャストルールが不明だとコード生成の品質が下がる。

*   **回答:**
    *   型変換禁止です。型変換は、標準ライブラリを別途提供し、その関数を利用します。なお、
    INT = signed 64-bit integer
    です。

## 4. `REF` の詳細仕様
*   **現状:** `14. Memory and Reference Model` に `REF` が存在するが、その具体的な意味が不明。
*   **不明点:**
    *   参照渡し（Pass-by-reference）としての機能なのか、それともポインタ的な概念なのか。
    *   ライフサイクルやスコープの外側からどのように参照を保持できるのか。
*   **回答:**
    *   14章に REF may only appear in a function parameter list.　および、The function modifies the caller's variable through the reference.と明記しております。

## 5. `OPTIONAL` / `RESULT` 型のインターフェース
*   **現状:** `08. Error_Handling.md` で言及はあるが、具体的なメンバやメソッド（`unwrap`, `is_success`, `value` 等）が定義されていない。
*   **不明点:**
    *   これらの型をどのように解体（Unwrap）して値を取り出すのか。決定論的であるためには、分岐が明示的である必要がある。
*   **回答:**
    *   現在の仕様で、OPTIONAL User は、User または、NONE。RESULT は、SUCCESSまたは、ERRORです。
    値の取り出しについては、「✅T.B.D.」に記載します。

## 6. 文字列の仕様
*   **現状:** 文字列の連結や操作についての仕様がない。
*   **不明点:**
    *   `+` 演算子で文字列連結を許可するのか。
    *   エスケープシーケンスの定義や、マルチライン文字列のサポート範囲。
*   **回答:**
    *   許可する。STRING + STRING -> STRING を許可
    *   STRING次のエスケープをサポートする。 
        \r, \n, \t, \\ \"
---

## 方針提案
上記項目について、`language-specification` を改定し、定義を追記するステップを踏むか、実装側で一時的に挙動を定義（デファクトスタンダード化）した後に仕様へフィードバックするかを決定する必要がある。
