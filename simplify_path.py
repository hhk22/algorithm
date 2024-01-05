

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        new_path_list = []
        for p in path_list:
            if p == '..':
                if new_path_list:
                    new_path_list.pop()
            elif p != '' and p != '.':
                new_path_list.append(p)

        return '/' + '/'.join(new_path_list)


path = "/a//b////c/d//././/.."
# "/a/b/c"
s = Solution()
rst = s.simplifyPath(path)
print(rst)
