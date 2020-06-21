from read_file import Read_File


class filter_df:
    '''
    描述：dataframe数据过滤
    实现日期：2020/06/21
    作者：xzx
    '''

    def __init__(self, filename):
        self.data_obj = Read_File(filename)

    def include_str_df(self, col, str_include):
        '''
        过滤包含特定字符的dataframe
        :param col: 待过滤列名
        :param str_include: 指定过滤字符
        :return: dataframe
        '''
        data = self.data_obj.main()
        result = data[data[col].str.contains(str_include) == True]
        return result

    def drop_repeat_df(self):
        '''
        去除重复行
        :return: dataframe
        '''
        data = self.data_obj.main()
        result = data.drop_duplicates()
        return result
        # drop_duplicates参数说明：
        # # drop_duplicates(subset=['A_ID', 'B_ID'], keep='first')
        # # 上面的命令去掉A_ID和B_ID列中重复的行，并保留重复出现的行中第一次出现的行
        # # 当keep = False时，就是去掉所有的重复行
        # # 当keep =‘first'时，就是保留第一次出现的重复行
        # # 当keep = 'last'时就是保留最后一次出现的重复行。

    def drop_repeat_df_col(self, col):
        '''
        去除特定列重复项
        :param col: 列名
        :return: dataframe
        '''
        data = self.data_obj.main()
        result = data.drop_duplicates([col])
        return result

    def replace_df_col(self, col, str_rep, target_str):
        '''
        替换指定列值的字符
        :param col: 列名
        :param str_rep: 需要替换的字符
        :param target_str: 新字符
        :return: dataframe
        '''
        data = self.data_obj.main()
        result = data[col].str.replace(str_rep, target_str)
        return result

    def replace_df(self, str_rep, target_str):
        '''
        替换指定字符（整体替换）
        :param str_rep: 需要替换的字符
        :param target_str: 新字符
        :return:
        '''
        data = self.data_obj.main()
        result = data.replace(str_rep, target_str, regex=True)
        return result

        # # 创建数据集
        # df = pd.DataFrame(
        #     {
        #         '名称': ['产品1', '产品2', '产品3', '产品4', '产品5', '产品6', '产品7', '产品8'],
        #         '数量': ['A', '0.7', '0.8', '0.4', '0.7', 'B', '0.76', '0.28'],
        #         '金额': ['0', '0.48', '0.33', 'C', '0.74', '0', '0', '0.22'],
        #         '合计': ['D', '0.37', '0.28', 'E', '0.57', 'F', '0', '0.06'],
        #     }
        # )
        #
        # # 搜索整个DataFrame, 并将所有符合条件的元素全部替换。操作之后，其实原DataFrame是并没有改变的。改变的只是一个复制品。
        # df.replace('A', 0.1)
        #
        # # 如果需要改变原数据，需要添加常用参数 inplace=True
        # df.replace('A', 0.1, inplace=True)
        #
        # # inplace这个参数在一般情况没多大用处，但是如果只替换部分区域时，inplace参数就有用了
        # df['金额'].replace(0, 0.22, inplace=True)
        # '''
        # 在上面这个操作中，‘合计’这一列中的0，并没有被替换。
        # 只有‘金额’这一列的0被替换，而且，替换后的结果不需要我们再和原数据进行合并操作，直接体现在原数据中。
        # '''
        #
        # # 可以用字典形式替换多个值
        # df.replace({'C': 0.9999, 'F': 0.7777})
        # df.replace(['C', 'F'], [0.999, 0.777])
        # df['合计'].replace({'D': 0.11111, 'F': 0.22222}, inplace=True)
        #
        # # 如果替换的值都是一样的话
        # df.replace(['C', 'F'], 0.33333)
        # df['合计'].replace(['D', 'F'], 0.0111, inplace=True)
        #
        # # 参数regex，可以使用正则表达式替换多个
        # df.replace('[A-Z]', 0.99, regex=True)
        #
        # # 只需要替换某个数据的部分内容
        # df['名称'].str.replace('产品', 'product')
        #
        # # 某些列满足特定条件，然后改变另外的某些列的值
        # df.loc[df['数量'] == 'A', '合计'] = 'changed'  # 关键句，直接改变df的值
        # df.loc[df['合计'].str.contains('change'), '数量'] = 'A'  # 使用countains可以用来正则匹配筛选


filter_data = filter_df('data.xlsx')
# col = '质量等级'
str_rep = '污染'
target_str = '危害'
data = filter_data.replace_df(str_rep, target_str)
print(data)
