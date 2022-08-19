from rest_framework.permissions import BasePermission

class IsXiaoMingPermission(BasePermission):
    """
    自定义权限，可用于全局配置，也可用于局部配置
    """
    def has_permission(self, request, view):
        """
        视图权限
        返回True则表示允许访问视图类
        request: 本次客户端提交的请求对象
        view, 本次客户端访问的视图类
        """
        user = request.query_params.get("user")
        return user == "xiaoming"