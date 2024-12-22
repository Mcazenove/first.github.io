

public class User {
private String uname;
private String pword;
private String sbyy;
//告诉C层能否登录,并告知C层失败原因
public boolean login() {
if(uname.equals("tom")) {

if(pword.equals("m123")) {
return true;
}else {
sbyy="密码错误,请重新输入密码”;
return false;

}
}
else {
sbyy="用户名不存在";
return false;

}
}


public User() {

public String getUname() {
return uname;
}

public void setUname(String uname) {
this.uname = uname;
}

public String getPword() {
return pword;
}

public void setPword(String pword) {
this. pword = pword;
}

public String getSbyy() {
return sbyy;
}

public void setSbyy(String sbyy) {
this.sbyy = sbyy;
}
}