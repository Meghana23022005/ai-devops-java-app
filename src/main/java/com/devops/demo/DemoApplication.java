package com.devops.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {
    public void brokenMethod() {
    int number = "AI";   // added error to invoke AI Agent
    }


    @GetMapping("/")
    public String home() {
        return "AI-Assisted DevOps Automation Project - Running Successfully";
    }

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
