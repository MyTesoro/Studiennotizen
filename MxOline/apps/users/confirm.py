import re


def pwd_re(pwd):
    i = 0
    noke = [0, 0, 0, 0]
    # 是否包含数字
    if re.match('^.*[0-9]+.*$', pwd):
        i += 1
        noke[0] = 1
    # 是否包含小写字母
    if re.match('^.*[a-z]+.*$', pwd):
        i += 1
        noke[1] = 1
    # 是否包含大写字母
    if re.match('^.*[A-Z]+.*$', pwd):
        i += 1
        noke[2] = 1
    # 是否包含特殊字符（非数字、字母的字符）
    if re.match("^.*[~`!@#$%^&*()_+|<>,.?/:;'\\[\\]{}\"]+.*$", pwd):
        i += 1
        noke[3] = 1

    if noke == [1, 1, 1, 1]:
        return True
    else:
        return False


def mobile_re(mobile):
    # 号码前缀，如果运营商启用新的号段，只需要在此列表将新的号段加上即可。
    phoneprefix = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '145', '147', '150', '151',
                   '152', '153', '155', '156', '158', '159', '170', '176', '178', '183', '182', '184', '185', '186',
                   '188', '187', '189']
    # 检测号码是否长度是否合法。

    if mobile.isdigit():
        # 检测前缀是否是正确。
        if mobile[:3] in phoneprefix:
            return True
        else:
            return False
