
var projectName = '在线借阅图书管理系统';
/**
 * 轮播图配置
 */
var swiper = {
	// 设定轮播容器宽度，支持像素和百分比
	width: '100%',
	height: '400px',
	// hover（悬停显示）
	// always（始终显示）
	// none（始终不显示）
	arrow: 'none',
	// default（左右切换）
	// updown（上下切换）
	// fade（渐隐渐显切换）
	anim: 'default',
	// 自动切换的时间间隔
	// 默认3000
	interval: 2000,
	// 指示器位置
	// inside（容器内部）
	// outside（容器外部）
	// none（不显示）
	indicator: 'outside'
}

/**
 * 个人中心菜单
 */
var centerMenu = [{
	name: '个人中心',
	url: '../' + localStorage.getItem('userTable') + '/center.html'
}, 
]


var indexNav = [

{
	name: '图书信息',
	url: './pages/tushuxinxi/list.html'
}, 
{
	name: '借阅记录',
	url: './pages/jieyuejilu/list.html'
}, 
{
	name: '归还记录',
	url: './pages/guihaijilu/list.html'
}, 
{
	name: '图书续借',
	url: './pages/tushuxujie/list.html'
}, 

{
	name: '留言板',
	url: './pages/messages/list.html'
}
]

var adminurl =  "http://localhost:8080/zxjyts/admin/dist/index.html";

var cartFlag = false

var chatFlag = false




var menu = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["新增","查看","修改","删除"],"menu":"读者","menuJump":"列表","tableName":"duzhe"}],"menu":"读者管理"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["新增","查看","修改","删除"],"menu":"图书分类","menuJump":"列表","tableName":"tushufenlei"}],"menu":"图书分类管理"},{"child":[{"appFrontIcon":"cuIcon-pic","buttons":["新增","查看","修改","删除","查看评论","借阅","归还","预借"],"menu":"图书信息","menuJump":"列表","tableName":"tushuxinxi"}],"menu":"图书信息管理"},{"child":[{"appFrontIcon":"cuIcon-goods","buttons":["新增","查看","修改","删除","续借","归还"],"menu":"借阅记录","menuJump":"列表","tableName":"jieyuejilu"}],"menu":"借阅记录管理"},{"child":[{"appFrontIcon":"cuIcon-explore","buttons":["新增","查看","修改","删除"],"menu":"归还记录","menuJump":"列表","tableName":"guihaijilu"}],"menu":"归还记录管理"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["新增","查看","修改","删除","审核"],"menu":"图书续借","menuJump":"列表","tableName":"tushuxujie"}],"menu":"图书续借管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看","修改","回复","删除"],"menu":"留言板管理","tableName":"messages"}],"menu":"留言板管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-link","buttons":["查看","查看评论","借阅","预借"],"menu":"图书信息列表","menuJump":"列表","tableName":"tushuxinxi"}],"menu":"图书信息模块"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看","续借"],"menu":"借阅记录列表","menuJump":"列表","tableName":"jieyuejilu"}],"menu":"借阅记录模块"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看"],"menu":"归还记录列表","menuJump":"列表","tableName":"guihaijilu"}],"menu":"归还记录模块"},{"child":[{"appFrontIcon":"cuIcon-skin","buttons":["查看"],"menu":"图书续借列表","menuJump":"列表","tableName":"tushuxujie"}],"menu":"图书续借模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-pic","buttons":["查看","查看评论","借阅","预借"],"menu":"图书信息","menuJump":"列表","tableName":"tushuxinxi"}],"menu":"图书信息管理"},{"child":[{"appFrontIcon":"cuIcon-goods","buttons":["查看","续借"],"menu":"借阅记录","menuJump":"列表","tableName":"jieyuejilu"}],"menu":"借阅记录管理"},{"child":[{"appFrontIcon":"cuIcon-explore","buttons":["查看"],"menu":"归还记录","menuJump":"列表","tableName":"guihaijilu"}],"menu":"归还记录管理"},{"child":[{"appFrontIcon":"cuIcon-copy","buttons":["查看"],"menu":"图书续借","menuJump":"列表","tableName":"tushuxujie"}],"menu":"图书续借管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-link","buttons":["查看","查看评论","借阅","预借"],"menu":"图书信息列表","menuJump":"列表","tableName":"tushuxinxi"}],"menu":"图书信息模块"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["查看","续借"],"menu":"借阅记录列表","menuJump":"列表","tableName":"jieyuejilu"}],"menu":"借阅记录模块"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看"],"menu":"归还记录列表","menuJump":"列表","tableName":"guihaijilu"}],"menu":"归还记录模块"},{"child":[{"appFrontIcon":"cuIcon-skin","buttons":["查看"],"menu":"图书续借列表","menuJump":"列表","tableName":"tushuxujie"}],"menu":"图书续借模块"}],"hasBackLogin":"否","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"读者","tableName":"duzhe"}]


var isAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].backMenu.length;j++){
                for(let k=0;k<menus[i].backMenu[j].child.length;k++){
                    if(tableName==menus[i].backMenu[j].child[k].tableName){
                        let buttons = menus[i].backMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}

var isFrontAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}
