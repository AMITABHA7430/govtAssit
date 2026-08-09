package com.sih.govassist.controller;

import com.sih.govassist.dto.request.LoginRequest;
import com.sih.govassist.dto.request.SignupRequest;
import com.sih.govassist.dto.response.LoginResponse;
import com.sih.govassist.service.AuthService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1/auth")
@CrossOrigin
public class AuthenticationController {

    private final AuthService service;

    public AuthenticationController(AuthService service) {
        this.service = service;
    }

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@Valid @RequestBody SignupRequest request) {

        System.out.println("SIGNUP CONTROLLER REACHED");

        try {

            service.signup(request);

            return ResponseEntity
                    .status(HttpStatus.CREATED)
                    .body("User registered successfully");

        } catch (Exception e) {

            e.printStackTrace();

            return ResponseEntity
                    .status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(e.getLocalizedMessage());

        }
    }
    @PostMapping("/login")
    public ResponseEntity<?> signup(@Valid @RequestBody LoginRequest request){
        System.out.println("LOGIN CONTROLLER REACHED");

        LoginResponse response =
                service.login(request);

        if (!response.isSuccess()) {
            return ResponseEntity
                    .status(HttpStatus.UNAUTHORIZED)
                    .body(response);
        }

        return ResponseEntity.ok(response);
    }


}
