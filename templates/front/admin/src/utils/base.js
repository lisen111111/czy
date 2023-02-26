const base = {
    get() {
        return {
            url : "http://localhost:8080/zxjyts/",
            name: "zxjyts",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "在线借阅图书管理系统"
        } 
    }
}
export default base
