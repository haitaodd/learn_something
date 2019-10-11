package controller;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    /**
     * 1.继承HttpServlet
     * 2.override doGet， 用于接受Get请求
     * 3.得到系统时间，放入HttpServletRequest中，转发给html
     * 4.使用WebServlet注解，对外发布服务
     */

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
    }
}
