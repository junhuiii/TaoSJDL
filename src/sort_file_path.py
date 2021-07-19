class FileSort:

    def __init__(self,info):
        self.info = info

    def sort_file_path(self, config, overall_info):
        if self.info['brand'] == '北海印象':
            if '花胶/鱼胶' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['bhyx_fm']
                overall_info.append(self.info)

        elif self.info['brand'] == '德叔鲍鱼':
            if '鲍鱼' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['dsby_ab']
                overall_info.append(self.info)

        elif self.info['brand'] == '官栈':
            if '花胶/鱼胶' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['gz_fm']
                overall_info.append(self.info)

        elif self.info['brand'] == '邻家燕':
            if '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['ljy_sc']
                overall_info.append(self.info)

        elif self.info['brand'] == '参王朝':
            if '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['swc_sc']
                overall_info.append(self.info)

        elif self.info['brand'] == '仙鹤岛':
            if '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['xhd_sc']
                overall_info.append(self.info)

        elif self.info['brand'] == '晓芹':
            if '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['xq_sc']
                overall_info.append(self.info)

        elif self.info['brand'] == 'xiaoqin aquatic product/晓琴水产':
            if '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['xqsc_sc']
                overall_info.append(self.info)

        elif self.info['brand'] == '忆角巷':
            if '花胶/鱼胶' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['yjx_fm']
                overall_info.append(self.info)

        elif self.info['brand'] == '燕印象':
            if '燕窝' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['yyx_bn']
                overall_info.append(self.info)

            elif '花胶/鱼胶' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['yyx_fm']
                overall_info.append(self.info)

        elif self.info['brand'] == '燕之屋':
            if '燕窝' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['yzw_bn']
                overall_info.append(self.info)

        elif self.info['brand'] == '正典燕窝':
            if '燕窝' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['zdyw_bn']
                overall_info.append(self.info)

        elif self.info['brand'] == '久年':
            if '花胶/鱼胶' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['jn_fm']
                overall_info.append(self.info)

            elif '海参' in self.info['category']:
                self.info['dest_path'] = config['file_dest']['jn_sc']
                overall_info.append(self.info)
        else:
            overall_info.append(self.info)
        return overall_info
