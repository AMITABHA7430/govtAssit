package com.sih.govassist.service;

import com.sih.govassist.dto.request.LoginRequest;
import com.sih.govassist.dto.request.SignupRequest;
import com.sih.govassist.dto.response.LoginResponse;
import com.sih.govassist.repository.UserRepository;
import com.sih.govassist.entity.User;
import com.sih.govassist.security.JWTService;
import com.sih.govassist.validator.SignupValidator;
import com.sih.govassist.validator.ValidationResult;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import com.sih.govassist.service.impl.AuthServiceIMP;
import org.springframework.stereotype.Service;
import java.util.Optional;

@Service
public class AuthService implements AuthServiceIMP {

    private final UserRepository userRepository;

    private final SignupValidator signupValidator;

    private final JWTService jwtService;

    public AuthService(UserRepository userRepository, SignupValidator signupValidator, JWTService jwtService) {
        this.userRepository = userRepository;
        this.signupValidator = signupValidator;
        this.jwtService = jwtService;
    }

    @Override
    public void signup(SignupRequest request) {


        ValidationResult result =
                signupValidator.validate(request);

        if (!result.isValid()) {
            throw new RuntimeException(result.getMessage());
        }



        User user = new User();

        user.setName(request.getName());
        user.setEmail(request.getEmail());

        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

        String encodedPassword =
                encoder.encode(request.getPassword());

        user.setPassword(encodedPassword);

        userRepository.save(user);
    }

    @Override
    public LoginResponse login(LoginRequest request) {
        Optional<User> optionalUser =
                userRepository.findByEmail(request.getEmail());

        if (optionalUser.isEmpty()) {

            return new LoginResponse(
                    false,
                    "Invalid email or password",
                    null
            );
        }

        User user = optionalUser.get();




        BCryptPasswordEncoder encoder =
                new BCryptPasswordEncoder();

        boolean passwordMatches =
                encoder.matches(
                        request.getPassword(),
                        user.getPassword()
                );

        if (!passwordMatches) {

            return new LoginResponse(
                    false,
                    "Invalid email or password",
                    null
            );
        }


        String token =
                jwtService.generateToken(user);

        return new LoginResponse(
                true,
                "Login successful",
                token
        );

    }


}
