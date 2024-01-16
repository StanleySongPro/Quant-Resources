def cal_smb_hml(df):
    # 划分大小市值公司
    df['SB'] = df['circ_mv'].apply(
        lambda x: 'B' if x >= df['circ_mv'].median() else 'S')

    # 求账面市值比：PB的倒数
    df['BM'] = 1 / df['pb']

    # 划分高、中、低账面市值比公司
    border_down, border_up = df['BM'].quantile([0.3, 0.7])
    df['HML'] = df.apply(
        lambda row: 'H' if row['BM'] >= border_up else ('L' if row['BM'] <= border_down else 'M'), axis=1)

    # 组合划分为6组
    df_SL = df[(df['SB'] == 'S') & (df['HML'] == 'L')]
    df_SM = df[(df['SB'] == 'S') & (df['HML'] == 'M')]
    df_SH = df[(df['SB'] == 'S') & (df['HML'] == 'H')]
    df_BL = df[(df['SB'] == 'B') & (df['HML'] == 'L')]
    df_BM = df[(df['SB'] == 'B') & (df['HML'] == 'M')]
    df_BH = df[(df['SB'] == 'B') & (df['HML'] == 'H')]

    # 计算各组收益率
    R_SL = (df_SL['pct_chg'] * df_SL['circ_mv'] /
            100).sum() / df_SL['circ_mv'].sum()
    R_SM = (df_SM['pct_chg'] * df_SM['circ_mv'] /
            100).sum() / df_SM['circ_mv'].sum()
    R_SH = (df_SH['pct_chg'] * df_SH['circ_mv'] /
            100).sum() / df_SH['circ_mv'].sum()
    R_BL = (df_BL['pct_chg'] * df_BL['circ_mv'] /
            100).sum() / df_BL['circ_mv'].sum()
    R_BM = (df_BM['pct_chg'] * df_BM['circ_mv'] /
            100).sum() / df_BM['circ_mv'].sum()
    R_BH = (df_BH['pct_chg'] * df_BH['circ_mv'] /
            100).sum() / df_BH['circ_mv'].sum()

    # 计算SMB, HML并返回
    smb = (R_SL + R_SM + R_SH - R_BL - R_BM - R_BH) / 3
    hml = (R_SH + R_BH - R_SL - R_BL) / 2
    return smb, hml
