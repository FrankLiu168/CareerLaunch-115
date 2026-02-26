CREATE TABLE IF NOT EXISTS 原始_交通事故_肇事者 (
    年月 VARCHAR(255),
    分局 VARCHAR(255),
    肇事者_第一當事人_男 INT,
    肇事者_第一當事人_女 INT,
    肇事者_第一當事人_不詳 INT,
    死亡人數_男 INT,
    死亡人數_女 INT,
    受傷人數_男 INT,
    受傷人數_女 INT,
    PRIMARY KEY (年月, 分局)
);