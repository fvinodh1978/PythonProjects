package com.tester.guiservices;

import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;

public class TestDemo1{
	
	WebDriver driver;

	@BeforeTest
	public void BT() {
		System.setProperty("webdriver.chrome.driver",  "C:\\Official\\MyProjects\\ExternalLibraries\\chromedriver.exe");
		System.out.println("This is Executed before Test...");
	}

	@Test
	public void testcase1() {
		System.out.println("This is 1st Testcase...");
	}
	
	@AfterTest
	public void AT() {
		System.out.println("This is Executed After Test...");
	}	
}
