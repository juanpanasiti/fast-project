from enum import Enum


class RoleEnum(str, Enum):
    SUPER = 'superadmin'
    ADMIN = 'admin'
    COMMON = 'common'


# Listas de roles
ADMIN_ROLES = [RoleEnum.ADMIN, RoleEnum.SUPER]
COMMON_ROLES = [RoleEnum.COMMON]
ALL_ROLES = [RoleEnum.ADMIN, RoleEnum.SUPER, RoleEnum.COMMON]
