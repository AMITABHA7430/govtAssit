package com.sih.govassist.service.impl;

import com.sih.govassist.dto.request.LoginRequest;
import com.sih.govassist.dto.request.SignupRequest;
import com.sih.govassist.dto.response.LoginResponse;


public interface AuthServiceIMP {

    void signup(SignupRequest request);
    LoginResponse login(LoginRequest request);
}


